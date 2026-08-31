
import streamlit as st
import random

# ============================================================
# MONDSTADT CHARACTER DATABASE
# ============================================================

characters = {

    "Albedo": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Blonde",
        "gender": "Male",
        "extra": "Geo"
        
    },

    "Amber": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Brown",
        "gender": "Female",
        "extra": "Pyro"
    },

    "Barbara": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Blonde",
        "gender": "Female",
        "extra": "Hydro"
    },

    "Bennett": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "White",
        "gender": "Male",
        "extra": "Pyro"
    },

    "Dahlia": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Pink",
        "gender": "Male",
        "extra": "Hydro"
    },

    "Diluc": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Red",
        "gender": "Male",
        "extra": "Pyro"
    },

    "Diona": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Pink",
        "gender": "Female",
        "extra": "Cryo"
    },

    "Durin": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "White",
        "gender": "Male",
        "extra": "Pyro"
    },

    "Eula": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Blue",
        "gender": "Female",
        "extra": "Cryo"
    },

    "Fischl": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Blonde",
        "gender": "Female",
        "extra": "Electro"
    },

    "Jean": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Blonde",
        "gender": "Female",
        "extra": "Anemo"
    },

    "Kaeya": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Blue",
        "gender": "Male",
        "extra": "Cryo"
    },

    "Klee": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Blonde",
        "gender": "Female",
        "extra": "Pyro"
    },

    "Lisa": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Purple",
        "gender": "Female",
        "extra": "Electro"
    },

    "Lohen": {
        "fandom": "Lohen",
        "weapon": "Lohen",
        "hair_colour": "Lohen",
        "gender": "Lohen",
        "extra": "Lohen"
    },

    "Mika": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Light Blue",
        "gender": "Male",
        "extra": "Cryo"
    },

    "Mona": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Dark Blue",
        "gender": "Female",
        "extra": "Hydro"
    },

    "Nicole": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "White",
        "gender": "Female",
        "extra": "Pyro"
    },

    "Noelle": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Silver",
        "gender": "Female",
        "extra": "Geo"
    },

    "Prune": {
"fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Purple",
        "gender": "Female",
        "extra": "Anemo"

    },

    "Razor": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Gray",
        "gender": "Male",
        "extra": "Electro"
    },

    "Rosaria": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Burgundy",
        "gender": "Female",
        "extra": "Cryo"
    },

    "Sucrose": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Mint",
        "gender": "Female",
        "extra": "Anemo"
    },

    "Venti": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Black",
        "gender": "Male",
        "extra": "Anemo"
    },
    

    "Baizhu": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Green",
        "gender": "Male",
        "extra": "Dendro"
    },

    "Beidou": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Brown",
        "gender": "Female",
        "extra": "Electro"
    },

    "Chongyun": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Light Blue",
        "gender": "Male",
        "extra": "Cryo"
    },

    "Gaming": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Dark Brown",
        "gender": "Male",
        "extra": "Pyro"
    },

    "Ganyu": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Blue",
        "gender": "Female",
        "extra": "Cryo"
    },

    "Hu Tao": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Brown",
        "gender": "Female",
        "extra": "Pyro"
    },

    "Keqing": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Purple",
        "gender": "Female",
        "extra": "Electro"
    },

    "Lan Yan": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Black",
        "gender": "Female",
        "extra": "Anemo"
    },

    "Ningguang": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "White",
        "gender": "Female",
        "extra": "Geo"
    },

    "Qiqi": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "White",
        "gender": "Female",
        "extra": "Cryo"
    },

    "Shenhe": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "White",
        "gender": "Female",
        "extra": "Cryo"
    },

    "Xiangling": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Dark Blue",
        "gender": "Female",
        "extra": "Pyro"
    },

    "Xianyun": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Black",
        "gender": "Female",
        "extra": "Anemo"
    },

    "Xiao": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Dark Teal",
        "gender": "Male",
        "extra": "Anemo"
    },

    "Xingqiu": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Blue",
        "gender": "Male",
        "extra": "Hydro"
    },

    "Xinyan": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Black",
        "gender": "Female",
        "extra": "Pyro"
    },

    "Yanfei": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Pink",
        "gender": "Female",
        "extra": "Pyro"
    },

    "Yaoyao": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Brown",
        "gender": "Female",
        "extra": "Dendro"
    },

    "Yelan": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Dark Blue",
        "gender": "Female",
        "extra": "Hydro"
    },

    "Yun Jin": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Black",
        "gender": "Female",
        "extra": "Geo"
    },

    "Zhongli": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Brown",
        "gender": "Male",
        "extra": "Geo"
    },

    "Zibai": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "White",
        "gender": "Female",
        "extra": "Geo"
    },
    

    "Arataki Itto": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "White",
        "gender": "Male",
        "extra": "Geo"
    },

    "Chiori": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Black",
        "gender": "Female",
        "extra": "Geo"
    },

    "Gorou": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Brown",
        "gender": "Male",
        "extra": "Geo"
    },

    "Kaedehara Kazuha": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "White",
        "gender": "Male",
        "extra": "Anemo"
    },

    "Kamisato Ayaka": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "White",
        "gender": "Female",
        "extra": "Cryo"
    },

    "Kamisato Ayato": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Light Blue",
        "gender": "Male",
        "extra": "Hydro"
    },

    "Kirara": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Blonde",
        "gender": "Female",
        "extra": "Dendro"
    },

    "Kujou Sara": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Black",
        "gender": "Female",
        "extra": "Electro"
    },

    "Kuki Shinobu": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Purple",
        "gender": "Female",
        "extra": "Electro"
    },

    "Raiden Shogun": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Purple",
        "gender": "Female",
        "extra": "Electro"
    },

    "Sangonomiya Kokomi": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Pink",
        "gender": "Female",
        "extra": "Hydro"
    },

    "Sayu": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Gray",
        "gender": "Female",
        "extra": "Anemo"
    },

    "Shikanoin Heizou": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Brown",
        "gender": "Male",
        "extra": "Anemo"
    },

    "Thoma": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Blonde",
        "gender": "Male",
        "extra": "Pyro"
    },

    "Yae Miko": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Pink",
        "gender": "Female",
        "extra": "Electro"
    },

    "Yoimiya": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Blonde",
        "gender": "Female",
        "extra": "Pyro"
    },

    "Yumemizuki Mizuki": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Pink",
        "gender": "Female",
        "extra": "Anemo"
    },
    

    "Alhaitham": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Gray",
        "gender": "Male",
        "extra": "Dendro"
    },

    "Candace": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Blue",
        "gender": "Female",
        "extra": "Hydro"
    },

    "Collei": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Green",
        "gender": "Female",
        "extra": "Dendro"
    },

    "Cyno": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "White",
        "gender": "Male",
        "extra": "Electro"
    },

    "Dehya": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Black",
        "gender": "Female",
        "extra": "Pyro"
    },

    "Dori": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Purple",
        "gender": "Female",
        "extra": "Electro"
    },

    "Faruzan": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Light Blue",
        "gender": "Female",
        "extra": "Anemo"
    },

    "Kaveh": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Blonde",
        "gender": "Male",
        "extra": "Dendro"
    },

    "Layla": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Dark Blue",
        "gender": "Female",
        "extra": "Cryo"
    },

    "Nahida": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "White",
        "gender": "Female",
        "extra": "Dendro"
    },

    "Nilou": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Red",
        "gender": "Female",
        "extra": "Hydro"
    },

    "Sethos": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "White",
        "gender": "Male",
        "extra": "Electro"
    },

    "Tighnari": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Black",
        "gender": "Male",
        "extra": "Dendro"
    },


    "Charlotte": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Blonde",
        "gender": "Female",
        "extra": "Cryo"
    },

    "Chevreuse": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Pink",
        "gender": "Female",
        "extra": "Pyro"
    },

    "Clorinde": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Dark Blue",
        "gender": "Female",
        "extra": "Electro"
    },

    "Emilie": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Blonde",
        "gender": "Female",
        "extra": "Dendro"
    },

    "Escoffier": {
"fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Orange",
        "gender": "Female",
        "extra": "Cryo"
    },

    "Freminet": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Light Blue",
        "gender": "Male",
        "extra": "Cryo"
    },

    "Furina": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "White",
        "gender": "Female",
        "extra": "Hydro"
    },


    "Lynette": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Gray",
        "gender": "Female",
        "extra": "Anemo"
    },

    "Lyney": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "White",
        "gender": "Male",
        "extra": "Pyro"
    },

    "Navia": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Blonde",
        "gender": "Female",
        "extra": "Geo"
    },

    "Neuvillette": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "White",
        "gender": "Male",
        "extra": "Hydro"
    },

    "Sigewinne": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Pink",
        "gender": "Female",
        "extra": "Hydro"
    },

    "Skirk": {
"fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "White",
        "gender": "Female",
        "extra": "Cryo"
    },

    "Wriothesley": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Black",
        "gender": "Male",
        "extra": "Cryo"
    },
    

    "Chasca": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Black",
        "gender": "Female",
        "extra": "Anemo"
    },

    "Citlali": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Pink",
        "gender": "Female",
        "extra": "Cryo"
    },

    "Iansan": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Gray",
        "gender": "Female",
        "extra": "Electro"
    },

    "Ifa": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Black",
        "gender": "Male",
        "extra": "Anemo"
    },

    "Kachina": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Brown",
        "gender": "Female",
        "extra": "Geo"
    },

    "Kinich": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Black",
        "gender": "Male",
        "extra": "Dendro"
    },

    "Mavuika": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Red",
        "gender": "Female",
        "extra": "Pyro"
    },

    "Mualani": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "White",
        "gender": "Female",
        "extra": "Hydro"
    },

    "Ororon": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Gray",
        "gender": "Male",
        "extra": "Electro"
    },

    "Varesa": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Brown",
        "gender": "Female",
        "extra": "Electro"
    },

    "Xilonen": {
        "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Blonde",
        "gender": "Female",
        "extra": "Geo"
    },
   

    "Aino": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Pink",
        "gender": "Female",
        "extra": "Hydro"
    },


    "Flins": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Purple",
        "gender": "Male",
        "extra": "Electro"
    },

    "Illuga": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Silver",
        "gender": "Male",
        "extra": "Geo"
    },

    "Ineffa": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "Light Blue",
        "gender": "Female",
        "extra": "Electro"
    },

    "Jahoda": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Blonde",
        "gender": "Female",
        "extra": "Anemo"
    },

    "Lauma": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "White",
        "gender": "Female",
        "extra": "Dendro"
    },

    "Linnea": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Pink",
        "gender": "Female",
        "extra": "Geo"
    },

    "Nefer": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Green",
        "gender": "Female",
        "extra": "Dendro"
    },
    

    "Pierro": {
        "fandom": "Genshin Impact",
        "weapon": "Not Playable",
        "hair_colour": "White",
        "gender": "Male",
        "extra": "Fatui"
    },

    "Capitano": {
        "fandom": "Genshin Impact",
        "weapon": "Not Playable",
        "hair_colour": "Black",
        "gender": "Male",
        "extra": "Dead"
    },

    "Dottore": {
        "fandom": "Genshin Impact",
        "weapon": "Not Playable",
        "hair_colour": "Blue",
        "gender": "Male",
        "extra": "Dead"
    },

    "Columbina": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Black",
        "gender": "Female",
        "extra": "Hydro"
    },

    "Arlecchino": {
        "fandom": "Genshin Impact",
        "weapon": "Polearm",
        "hair_colour": "White",
        "gender": "Female",
        "extra": "Pyro"
    },

    "Scaramouche": {
        "fandom": "Genshin Impact",
        "weapon": "Catalyst",
        "hair_colour": "Dark Blue",
        "gender": "Male",
        "extra": "Anemo"
    },

    "Sandrone": {
        "fandom": "Genshin Impact",
        "weapon": "Claymore",
        "hair_colour": "Blonde",
        "gender": "Female",
        "extra": "Cryo"
    },

    "La Signora": {
        "fandom": "Genshin Impact",
        "weapon": "Not Playable",
        "hair_colour": "Blonde",
        "gender": "Female",
        "extra": "Dead"
    },

    "Pantalone": {
        "fandom": "Genshin Impact",
        "weapon": "Not Playable",
        "hair_colour": "Black",
        "gender": "Male",
        "extra": "Fatui"
    },

    "Tartaglia": {
        "fandom": "Genshin Impact",
        "weapon": "Bow",
        "hair_colour": "Orange",
        "gender": "Male",
        "extra": "Hydro"
    },

    "Odette": {
 "fandom": "Genshin Impact",
        "weapon": "Sword",
        "hair_colour": "Light Blue",
        "gender": "Female",
        "extra": "Cryo"
    },

    "Alyosha":{
         "fandom": "Genshin Impact",
                "weapon": "Polearm",
                "hair_colour": "Mint Green",
                "gender": "Male",
                "extra": "Electro"
    },
    "Bennets Parents": {
 "fandom": "Genshin Impact",
                "weapon": "Not Playable",
                "hair_colour": "Grey",
                "gender": "Male and Female",
                "extra": "Dead"
    },

    "Hatsune Miku": {
    "fandom": "Project Sekai",
    "weapon": "Virtual Singer",
    "hair_colour": "Blue",
    "gender": "Female",
    "extra": "Virtual Singer"
},

"Kagamine Rin": {
    "fandom": "Project Sekai",
    "weapon": "Virtual Singer",
    "hair_colour": "Blonde",
    "gender": "Female",
    "extra": "Virtual Singer"
},

"Kagamine Len": {
    "fandom": "Project Sekai",
    "weapon": "Virtual Singer",
    "hair_colour": "Blonde",
    "gender": "Male",
    "extra": "Virtual Singer"
},

"Megurine Luka": {
    "fandom": "Project Sekai",
    "weapon": "Virtual Singer",
    "hair_colour": "Pink",
    "gender": "Female",
    "extra": "Virtual Singer"
},

"MEIKO": {
    "fandom": "Project Sekai",
    "weapon": "Virtual Singer",
    "hair_colour": "Brown",
    "gender": "Female",
    "extra": "Virtual Singer"
},

"KAITO": {
    "fandom": "Project Sekai",
    "weapon": "Virtual Singer",
    "hair_colour": "Blue",
    "gender": "Male",
    "extra": "Virtual Singer"
},


"Ichika Hoshino": {
    "fandom": "Project Sekai",
    "weapon": "Guitar / Vocal",
    "hair_colour": "Black",
    "gender": "Female",
    "extra": "Leo/need"
},

"Saki Tenma": {
    "fandom": "Project Sekai",
    "weapon": "Keyboard",
    "hair_colour": "Pink",
    "gender": "Female",
    "extra": "Leo/need"
},

"Honami Mochizuki": {
    "fandom": "Project Sekai",
    "weapon": "Drums",
    "hair_colour": "Peach",
    "gender": "Female",
    "extra": "Leo/need"
},

"Shiho Hinomori": {
    "fandom": "Project Sekai",
    "weapon": "Bass",
    "hair_colour": "Light Green",
    "gender": "Female",
    "extra": "Leo/need"
},


"Minori Hanasato": {
    "fandom": "Project Sekai",
    "weapon": "Vocalist",
    "hair_colour": "Brown",
    "gender": "Female",
    "extra": "MORE MORE JUMP!"
},

"Haruka Kiritani": {
    "fandom": "Project Sekai",
    "weapon": "Vocalist",
    "hair_colour": "Blue",
    "gender": "Female",
    "extra": "MORE MORE JUMP!"
},

"Airi Momoi": {
    "fandom": "Project Sekai",
    "weapon": "Vocalist",
    "hair_colour": "Pink",
    "gender": "Female",
    "extra": "MORE MORE JUMP!"
},

"Shizuku Hinomori": {
    "fandom": "Project Sekai",
    "weapon": "Vocalist",
    "hair_colour": "Blue",
    "gender": "Female",
    "extra": "MORE MORE JUMP!"
},


"Kohane Azusawa": {
    "fandom": "Project Sekai",
    "weapon": "Vocalist",
    "hair_colour": "Brown",
    "gender": "Female",
    "extra": "Vivid BAD SQUAD"
},

"An Shiraishi": {
    "fandom": "Project Sekai",
    "weapon": "Vocalist",
    "hair_colour": "Brown",
    "gender": "Female",
    "extra": "Vivid BAD SQUAD"
},

"Akito Shinonome": {
    "fandom": "Project Sekai",
    "weapon": "Vocalist",
    "hair_colour": "Orange",
    "gender": "Male",
    "extra": "Vivid BAD SQUAD"
},

"Toya Aoyagi": {
    "fandom": "Project Sekai",
    "weapon": "Vocalist",
    "hair_colour": "Blue",
    "gender": "Male",
    "extra": "Vivid BAD SQUAD"
},


"Tsukasa Tenma": {
    "fandom": "Project Sekai",
    "weapon": "Show Performer",
    "hair_colour": "Blonde",
    "gender": "Male",
    "extra": "Wonderlands × Showtime"
},

"Emu Otori": {
    "fandom": "Project Sekai",
    "weapon": "Show Performer",
    "hair_colour": "Pink",
    "gender": "Female",
    "extra": "Wonderlands × Showtime"
},

"Nene Kusanagi": {
    "fandom": "Project Sekai",
    "weapon": "Vocalist",
    "hair_colour": "Green",
    "gender": "Female",
    "extra": "Wonderlands × Showtime"
},

"Rui Kamishiro": {
    "fandom": "Project Sekai",
    "weapon": "Stage Director",
    "hair_colour": "Purple",
    "gender": "Male",
    "extra": "Wonderlands × Showtime"
},


"Kanade Yoisaki": {
    "fandom": "Project Sekai",
    "weapon": "Composer",
    "hair_colour": "White",
    "gender": "Female",
    "extra": "N25"
},

"Mafuyu Asahina": {
    "fandom": "Project Sekai",
    "weapon": "Lyricist",
    "hair_colour": "Dark Blue",
    "gender": "Female",
    "extra": "N25"
},

"Ena Shinonome": {
    "fandom": "Project Sekai",
    "weapon": "Illustrator",
    "hair_colour": "Brown",
    "gender": "Female",
    "extra": "N25"
},

"Mizuki Akiyama": {
    "fandom": "Project Sekai",
    "weapon": "Video Editor",
    "hair_colour": "Pink",
    "gender": "Unknown",
    "extra": "N25"
},
"Mizi": {
    "fandom": "ALIEN STAGE",
    "weapon": "Anakt Garden / Alien Stage",
    "hair_colour": "Pink",
    "gender": "Female",
    "extra": "Alive"
},

"Sua": {
    "fandom": "ALIEN STAGE",
    "weapon": "Anakt Garden / Alien Stage",
    "hair_colour": "Black",
    "gender": "Female",
    "extra": "Dead"
},

"Till": {
    "fandom": "ALIEN STAGE",
    "weapon": "Anakt Garden / Rebellion",
    "hair_colour": "Gray",
    "gender": "Male",
    "extra": "Alive"
},

"Ivan": {
    "fandom": "ALIEN STAGE",
    "weapon": "Anakt Garden / Alien Stage",
    "hair_colour": "Black",
    "gender": "Male",
    "extra": "Dead"
},

"Hyuna": {
    "fandom": "ALIEN STAGE",
    "weapon": "Anakt Garden / Rebellion",
    "hair_colour": "Dark Brown",
    "gender": "Female",
    "extra": "Dead"
},

"Luka": {
    "fandom": "ALIEN STAGE",
    "weapon": "Anakt Garden / Alien Stage",
    "hair_colour": "Blonde",
    "gender": "Male",
    "extra": "Alive"
},
}






    

            
    


    
    


# ============================================================
# PAGE SETUP
# ============================================================

st.set_page_config(
    page_title="Character Wordle",
    layout="wide"
)

st.title("Character Wordle")
st.subheader("Good Luck!")
st.write("Guess the mystery character!")


# ============================================================
# GAME SETUP
# ============================================================

character_list = list(characters.keys())

# Automatically choose the first character
if "secret" not in st.session_state:
    st.session_state.secret = random.choice(character_list)

# Store guesses
if "guesses" not in st.session_state:
    st.session_state.guesses = []

secret = st.session_state.secret


# ============================================================
# GUESS INPUT
# ============================================================

guess = st.selectbox(
    "Choose a character:",
    [""] + character_list,
    key="character_guess"
)

if st.button("Guess", type="primary"):

    if guess == "":
        st.warning("Please choose a character!")

    elif guess in st.session_state.guesses:
        st.warning("You already guessed that character!")

    else:

        st.session_state.guesses.append(guess)

        # ----------------------------------------------------
        # CORRECT GUESS
        # ----------------------------------------------------

        if guess == secret:

            st.success(
                f"🎉 Correct! The character was **{secret}**!"
            )

            st.balloons()

            # Don't choose the same character twice in a row
            available_characters = [
                character
                for character in character_list
                if character != secret
            ]

            # Choose the next character
            st.session_state.secret = random.choice(
                available_characters
            )

            # Clear guesses for the new round
            st.session_state.guesses = []

            st.rerun()


# ============================================================
# DISPLAY GUESSES
# ============================================================

if len(st.session_state.guesses) > 0:

    st.subheader("Your guesses")

    # Header row
    cols = st.columns(6)

    headers = [
        "Character",
        "Fandom",
        "Weapon",
        "Hair Colour",
        "Gender",
        "Extra"
    ]

    for col, header in zip(cols, headers):
        col.markdown(f"**{header}**")


    # Display every guess
    for guessed_character in st.session_state.guesses:

        data = characters[guessed_character]
        secret_data = characters[secret]

        cols = st.columns(6)

        # ----------------------------------------------------
        # CHARACTER
        # ----------------------------------------------------

        cols[0].write(guessed_character)


        # ----------------------------------------------------
        # FANDOM
        # ----------------------------------------------------

        if data["fandom"] == secret_data["fandom"]:
            cols[1].success(data["fandom"])
        else:
            cols[1].error(data["fandom"])


        # ----------------------------------------------------
        # WEAPON
        # ----------------------------------------------------

        if data["weapon"] == secret_data["weapon"]:
            cols[2].success(data["weapon"])
        else:
            cols[2].error(data["weapon"])


        # ----------------------------------------------------
        # HAIR COLOUR
        # ----------------------------------------------------

        if data["hair_colour"] == secret_data["hair_colour"]:
            cols[3].success(data["hair_colour"])
        else:
            cols[3].error(data["hair_colour"])


        # ----------------------------------------------------
        # GENDER
        # ----------------------------------------------------

        if data["gender"] == secret_data["gender"]:
            cols[4].success(data["gender"])
        else:
            cols[4].error(data["gender"])


        # ----------------------------------------------------
        # EXTRA
        # ----------------------------------------------------

        if data["extra"] == secret_data["extra"]:
            cols[5].success(data["extra"])
        else:
            cols[5].error(data["extra"])


# ============================================================
# NEW GAME BUTTON
# ============================================================

st.divider()

if st.button("🔄 New Game"):

    # Choose a different character
    available_characters = [
        character
        for character in character_list
        if character != st.session_state.secret
    ]

    st.session_state.secret = random.choice(
        available_characters
    )

    # Clear guesses
    st.session_state.guesses = []

    st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    " • Unlimited Mode • "
    "A new character is chosen after every correct guess."
)


