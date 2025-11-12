#Importation of necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import os
import folium as fol

#Creating necessary directories
os.makedirs("../Images",exist_ok=True)

#Reading the CSV file directly with pandas
df=pd.read_csv("experimentations_5G.csv",sep=";",encoding="ISO-8859-1")

#Function to convert frequency strings to float
def conver(val_str):
    try:
        return float(val_str.split()[0].replace(',','.')) # Convert string to float, replacing comma with dot
    except:
        return None

#Apply conversion to 'Bande de fréquences'
df["Bande de Frequence"]=df["Bande de fréquences"].apply(conver)
df["Latitude"] = df["Latitude"].apply(conver)
df["Longitude"] = df["Longitude"].apply(conver)

#Keep only necessary columns and rename them
df=df.rename(columns={"Expérimentateur":"Opérateur","Région":"Régions","Fréquences attribuées (limite haute)":"Frequence haute","Fréquences attribuées (limite basse)":"Frequence basse"})
df=df[["Régions","Opérateur","Bande de Frequence","Frequence haute","Frequence basse","Longitude","Latitude"]]

#Create a folium map centered around the mean latitude and longitude
map_5G=fol.Map(location=[df["Latitude"].mean(),df["Longitude"].mean()],zoom_start=6)

#Add markers for each experimentation point
regionss=sorted(df["Régions"].unique())
for reg in regionss:
    df1=df[df["Régions"]==reg].drop(columns=["Régions"]) # Filtering data for the region
    print(reg)
    
    #Saving table as image
    fig,ax=plt.subplots(figsize=(10,len(df1)*0.5+1)) #Dynamic height based on number of rows
    ax.axis("off")
    tbl=ax.table(cellText=df1.values,colLabels=df1.columns,cellLoc="center",loc="center") #Creating the table
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8)
    plt.savefig(f"../Images/tableau_{reg}.png",bbox_inches="tight",pad_inches=0.02,dpi=200,transparent=True,) #Saving the table as an image
    plt.close(fig)
    
    #Creating the bar graph
    plt.figure()
    plt.bar(df1["Opérateur"],df1["Bande de Frequence"],color="purple")
    plt.title(f"Expérimentations 5G-{reg}")
    plt.xlabel("Opérateur")
    plt.ylabel("Bande de fréquence (GHz)")
    plt.xticks(rotation=90) #Rotating x-axis labels for better readability
    plt.savefig(f"../Images/bar_{reg}.png",bbox_inches="tight",dpi=200,transparent=True) #Saving the bar graph
    plt.close()

    # Calculating mean latitude and longitude for marker placement
    lat=df1["Latitude"].mean()
    lon=df1["Longitude"].mean()

    #Creating popup HTML with link to region page
    page_html=f"../HTML/{reg}.html" #Path to the region-specific HTML page
    popup_html=f'<a href="{page_html}"target="_blank">{reg}</a>' #Creating the popup HTML with link
    fol.Marker([lat,lon],popup=popup_html).add_to(map_5G) #Adding marker to the map

#Saving the final map as an HTML file
map_5G.save("../HTML/Carte.html")