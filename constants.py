digits = "0123456789"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

spaces = [" ", "\n"]

operators = {
    "+" : "ADD",
    "-" : "SUBTRACT",
    "*" : "MULTIPLY",
    "/" : "DIVIDE",
    "%" : "MODULO",
    "^" : "EXPONENT",
    "=" : "ASSIGN",
    "+=" : "ADDASSIGN",
    "-=" : "SUBTRACTASSIGN",
    "*=" : "MULTIPLYASSIGN",
    "/=" : "DIVIDEASSIGN",
    "%=" : "MODULOASSIGN",
    "==" : "EQUAL",
    "!=" : "NOTEQUAL",
    "<" : "LESSERTHAN",
    ">" : "GREATERTHAN",
    "<=" : "LESSEROREQUAL",
    ">=" : "GREATEROREQUAL",
    "!" : "NOT",
    "&&": "AND",
    "||": "NOT",
    "==>" : "BALANCINGARROW"
}

keywords = [
    "assuming",
    "break",
    "class",
    "continue",
    "except",
    "import",
    "in",
    "ins",
    "iter",
    "none",
    "out",
    "pass",
    "return",
    "than",
    "try",
    "unless",
    "while"
]

special_characters = {
    "/" : "COMMENT",
    "#" : "MULTILINECOMMENT",
    "\\" : "BACKSLASH",
    '"' : "QUOTATIONMARK",
    "'" : "APOSTROPHE",
    "*": "ASTERISK",
    "?" : "QUESTIONMARK",
    "{" : "LEFTCURLYBRACE",
    "}" : "RIGHTCURLYBRACE",
    "(" : "LEFTROUNDBRACKET",
    ")" : "RIGHTROUNDBRACKET",
    "[" : "LEFTSQUAREBRACKET",
    "]" : "RIGHTSQUAREBRACKET",
    "`" : "BACKTICK"
}

comments = {
    "/" : "COMMENT",
    "#" : "MULTILINECOMMENT"
}

delimeters = {
    ";" : "SEMICOLON",
    "," : "COMMA"
}

booleans = {
    "true",
    "false"
}

atomic_number = ["*1", "*2", "*3", "*4", "*5", "*6", "*7", "*8", "*9", "*10", "*11", "*12", "*13", "*14", "*15", "*16", "*17", "*18", "*19", "*20", "*21", "*22", "*23", "*24", "*25", "*26", "*27", "*28", "*29", "*30", "*31", "*32", "*33", "*34", "*35", "*36", "*37", "*38", "*39", "*40", "*41", "*42", "*43", "*44", "*45", "*46", "*47", "*48", "*49", "*50", "*51", "*52", "*53", "*54", "*55", "*56", "*57", "*58", "*59", "*60", "*61", "*62", "*63", "*64", "*65", "*66", "*67", "*68", "*69", "*70", "*71", "*72", "*73", "*74", "*75", "*76", "*77", "*78", "*79", "*80", "*81", "*82", "*83", "*84", "*85", "*86", "*87", "*88", "*89", "*90", "*91", "*92", "*93", "*94", "*95", "*96", "*97", "*98", "*99", "*100", "*101", "*102", "*103", "*104", "*105", "*106", "*107", "*108", "*109", "*110", "*111", "*112", "*113", "*114", "*115", "*116", "*117", "*118"]


atomic_symbol = ["*H", "*He", "*Li", "*Be", "*B", "*C", "*N", "*O", "*F", "*Ne", "*Na", "*Mg", "*Al", "*Si", "*P", "*S", "*Cl", "*Ar", "*K", "*Ca", "*Sc", "*Ti", "*V", "*Cr", "*Mn", "*Fe", "*Co", "*Ni", "*Cu", "*Zn", "*Ga", "*Ge", "*As", "*Se", "*Br", "*Kr", "*Rb", "*Sr", "*Y", "*Zr", "*Nb", "*Mo", "*Tc", "*Ru", "*Rh", "*Pd", "*Ag", "*Cd", "*In", "*Sn", "*Sb", "*Te", "*I", "*Xe", "*Cs", "*Ba", "*La", "*Ce", "*Pr", "*Nd", "*Pm", "*Sm", "*Eu", "*Gd", "*Tb", "*Dy", "*Ho", "*Er", "*Tm", "*Yb", "*Lu", "*Hf", "*Ta", "*W", "*Re", "*Os", "*Ir", "*Pt", "*Au", "*Hg", "*Tl", "*Pb", "*Bi", "*Po", "*At", "*Rn", "*Fr", "*Ra", "*Ac", "*Th", "*Pa", "*U", "*Np", "*Pu", "*Am", "*Cm", "*Bk", "*Cf", "*Es", "*Fm", "*Md", "*No", "*Lr"]


atomic_name = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"]


compound_name = ['Acetic acid', 'Hydrochloric acid', 'Sulfuric acid', 'Acetate Ammonia', 'Nitric acid', 'Phosphoric acid', 'Sodium phosphate', 'Calcium carbonate', 'Ammonium sulfate', 'Carbonic acid', 'Sodium bicarbonate', 'Sodium hydroxide', 'Calcium hydroxide', 'Ethanol', 'Hydrobromic acid', 'Nitrous acid', 'Potassium hydroxide', 'Silver nitrate', 'Sodium carbonate', 'Sodium chloride', 'Cellulose', 'Magnesium hydroxide', 'Methane', 'Nitrogen dioxide', 'Sodium nitrate', 'Sulfurous acid', 'Aluminium sulfate', 'Aluminum oxide', 'Ammonium nitrate', 'Ammonium phosphate', 'Barium hydroxide', 'Carbon tetrachloride', 'Citric acid', 'Hydrocyanic acid', 'Salicylic Acid', 'Hydroiodic acid', 'Hypochlorous acid', 'Iron iii oxide', 'Magnesium phosphate', 'Sodium acetate', 'Sodium sulfate', 'Sucrose', 'Potassium nitrate', 'Ammonium bicarbonate', 'Ammonium chloride', 'Ammonium hydroxide', 'Calcium nitrate', 'Calcium oxide', 'Carbon monoxide', 'Chlorine gas', 'Phenol', 'Hydrogen peroxide', 'Hydroxide Magnesium chloride', 'Potassium chloride', 'Potassium iodide', 'Sulfur dioxide', 'Glycerin', 'Barium nitrate', 'Calcium acetate', 'Iron oxide', 'Potassium carbonate', 'Silver chloride', 'Sodium iodide', 'Sodium oxide', 'Sodium sulfide', 'Zinc nitrate', 'Phenolphthalein', 'Magnesium nitrate', 'Silicon dioxide', 'Acetone', 'Hydroquinone', 'Pyridine', 'Ammonium acetate', 'Xylene', 'Barium sulfate', 'Benzene', 'Bicarbonate', 'Chromate', 'Methyl', 'Ethyl', 'Ketone', 'Cyanide', 'Trichloroacetic acid', 'Magnesium sulfate', 'Methanol Oxygen', 'Methylene blue', 'Sodium sulfite', 'Sulfur trioxide', 'Aluminum phosphate', 'Stearic acid', 'Dinitrogen monoxide', 'Titanium dioxide', 'Acetonitrile', 'Oxalic acid', 'Potassium dichromate', 'Sodium bromide', 'Sodium hypochlorite', 'Zinc acetate', 'Zinc chloride', 'Zinc hydroxide', 'Magnesium carbonate', 'Potassium chlorate', 'Hydrazine', 'Ascorbic acid', 'Benzoic acid', 'Resorcinol', 'Chlorine', 'Maleic acid', 'Sodium metabisulfite', 'Acetamide', 'Sodium silicate', 'Nitrite', 'Phosphate', 'Dichloromethane', 'Carbon', 'Disulfide', 'Potassium chromate', 'Zinc sulfate', 'Iodine', 'Tannic acid', 'Aluminum', 'Perchloric acid', 'Hypochlorite', 'Potassium', 'Bromide', 'Chromic acid', 'Dihydrogen monoxide', 'Methyl acetate', 'Dimethyl sulfoxide', 'Hexane', 'Eugenol', 'Manganese dioxide', 'Lactic acid', 'Sodium potassium tartrate', 'Hexamine', 'Lithium hydroxide', 'Phosphorus pentachloride', 'Potassium oxide', 'Monopotassium phosphate', 'Silver acetate', 'Sodium citrate', 'Sodium fluoride', 'Sodium nitrite', 'Sulfate ion', 'Barium carbonate', 'Calcium iodide', 'Hydrogen sulfate', 'Lithium oxide', 'Dimethylglyoxime', 'Potassium', 'Permanganate', 'Silver phosphate', 'Ammonium bromide', 'Calcium phosphate', 'Dichromate', 'Aluminum sulfide', 'Ammonium carbonate', 'Barium chloride', 'Nitrogen monoxide', 'Fructose', 'Magnesium iodide', 'Magnesium sulfide', 'Ozone', 'Potassium cyanide', 'Silver oxide', 'Sodium chromate', 'Sodium peroxide', 'Toluene', 'Zinc carbonate', 'Zinc phosphate', 'Zinc sulfide', 'Para dichlorobenzene', 'Boric acid', 'Oxalate', 'Potassium bicarbonate', 'Potassium hypochlorite', 'Potassium nitrite', 'Bromothymol', 'Blue', 'Ammonium iodide', 'Ammonium nitrite', 'Ammonium oxide', 'Argon gas', 'Barium bromide', 'Barium iodide', 'Bromate', 'Dinitrogen trioxide', 'Ethylene glycol', 'Nickel sulfate', 'Helium', 'Iodide', 'Lead ii acetate', 'Lithium chloride', 'Phosphate ion', 'Potassium fluoride', 'Potassium sulfite', 'Silver carbonate', 'Sodium cyanide', 'Sodium nitride', 'Strontium chloride', 'Strontium nitrate', 'Urea', 'Bleach', 'Lithium bromide', 'Aluminum fluoride', 'Barium fluoride', 'Butanoic acid', 'Calcium hydride', 'Copper ii carbonate', 'Fluorine', 'Lithium phosphate', 'Glycerol', 'Hypobromous acid', 'Hypoiodous acid', 'Lead iodide', 'Lithium iodide', 'Magnesium oxide', 'Urethane', 'Nickel nitrate', 'Sodium dichromate', 'Tartaric acid', 'Zinc iodide', 'Bromine', 'Aluminum bromide', 'Sodium Percarbonate', 'Nickel acetate', 'Sodium Thiosulfate', 'Acetaldehyde', 'Copper sulfate', 'Mannitol', 'Calcium Chloride', 'Monosodium glutamate', 'Polystyrene', 'Calcium carbide', 'Tetrachloroethylene', 'Sodium Chlorate', 'Potassium Iodate', 'Lead Acetate', 'Potassium Thiocyanate', 'Butane', 'Maltose', 'Polyurethane Foam', 'Formaldehyde', 'Formic', 'Acid', 'Sulfur', 'Hexafluoride', 'Phosphorus', 'Trichloride', 'Ethane', 'Dinitrogen', 'Pentoxide', 'Phosphorous Acid', 'Potassium Ferrocyanide', 'Xenon Difluoride', 'Diatomic Bromine', 'Phenyl', 'Phosphorus Triiodide', 'Peroxydisulfuric', 'Acid', 'Dipotassium Phosphate', 'Aluminium hydroxide', 'Ammonium persulfate', 'Sodium borate', 'Chloroacetic acid', 'Potassium acetate', 'Barium oxide', 'Copper(I) Oxide', 'Copper Hydroxide', 'Tin Oxide', 'Chlorine Trifluoride', 'Ethylene', 'Acetylene', 'Chromic Oxide', 'Sodium bisulfate', 'Copper(II) chloride', 'Mercuric chloride', 'Tin(II) chloride', 'Propane', 'Lead(IV) oxide']

molecular_formula = ['CH3COOH', 'HCl', 'H2SO4', 'CH3COO–', 'NH3', 'HNO3', 'H3PO4', 'Na3PO4', 'CaCO3', '(NH4)2SO4', 'H2CO3', 'NaHCO3', 'NaOH', 'Ca(OH)2', 'C2H5OH', 'HBr', 'HNO2', 'KOH', 'AgNO3', 'Na2CO3', 'NaCl', '(C6H10O5)n', 'Mg(OH)2', 'CH4', 'NO2', 'NaNO3', 'H2SO3', 'Al2(SO4)3', 'Al2O3', 'NH4NO3', '(NH4)3PO4', 'Ba(OH)2', 'CCl4', 'C6H8O7', 'HCN', 'C7H6O3', 'HI', 'HClO', 'Fe2O3', 'Mg3(PO4)2', 'C2H3NaO2', 'Na2SO4', 'C12H22O11', 'KNO3', 'NH4HCO3', 'NH4Cl', 'NH4OH', 'Ca(NO3)2', 'CaO', 'CO', 'Cl2', 'C6H6O', 'H2O2', 'OH–', 'MgCl2', 'KCl', 'KI', 'SO2', 'C3H8O3', 'Ba(NO3)2', 'C4H6O4Ca', 'Fe2O3', 'K2CO3', 'AgCl', 'NaI', 'Na2O', 'Na2S', 'Zn(NO3)2', 'C20H14O4', 'Mg(NO3)2', 'SiO2', 'C3H6O', 'C6H6O2', 'C5H5N', 'C2H3O2NH4', 'C8H10', 'BaSO4', 'C6H6', 'CHO3–', 'CrO42-', 'C4H8O', 'CN−', 'C2HCl3O2', 
'MgSO4', 'CH3OH', 'O', 'C16H18ClN3S', 'Na2SO3', 'SO3', 'AlPO4', 'C18H36O2', 'N2O', 'TiO2', 'C2H3N', 'H2C2O4', 'K2Cr2O7', 'NaBr',
'NaClO', 'Zn(CH3COO)2(H2O)2', 'ZnCl2', 'Zn(OH)2', 'MgCO3', 'KClO3', 'N2H4', 'C6H8O6', 'C7H6O2', 'C6H6O2', 'Cl2', 'C4H4O4', 'Na2S2O5', 'C2H5NO', '(Na2O)x·SiO2', 'NO2−', 'PO43-', 'CH2Cl2', 'CS2', 'CrK2O4', 'ZnSO4', 'I', 'C76H52O46', 'Al', 'HClO4', 'ClO–', 'KBr', 'H2CrO4', 'OH2', 'C3H6O2', 'C2H6OS', 'C6H14', 'C10H12O2', 'MnO2', 'C3H6O3', 'C4H4O6KNa·4H2O', 'C6H12N4', 'LiOH', 'PCl5', 'K2O', 'KH2PO4', 'AgC2H3O2', 'Na3C6H5O7', 'NaF', 'NaNO2', 'SO42−', 'BaCO3', 'CaI2', 'HSO4–', 'Li2O', 'C4H8N2O2', 'KMnO4', 'Ag3PO4', 'NH4Br', 'Ca3(PO4)2', 'K2Cr2O7', 'Al2S3', '(NH4)2CO3', 'BaCl2', 'NO', 'C6H12O6', 'MgI2', 'MgS', 'O3', 'KCN', 'Ag2O', 'Na2CrO4', 'Na2O2', 'C7H8', 'ZnCO3', 'Zn3(PO4)2', 'ZnS', 'C6H4Cl2', 'H3BO3', 'C2O42−', 'KHCO3', 'KClO', 'KNO2', 'C27H28Br2O5S', 'NH4I', 'NH4NO2', '(NH4)2O', 'Ar', 'BaBr2', 'BaI2', 'BrO3–', 'N2O3', 'C2H6O2', 'NiSO4', 'He', 'I–', 'Pb(C2H3O2)2', 'LiCl', 'PO43-', 'KF', 'K2SO3', 'Ag2CO3', 'NaCN', 'Na3N', 'SrCl2', 'Sr(NO3)2', 'CH4N2O', 'NaClO', 'LiBr', 'AlF3', 'BaF2', 'C4H8O2', 'CaH2', 'CuCO3', 'F', 'Li3PO4', 'C3H8O3', 'HBrO', 'HIO', 'PbI2', 'LiI', 'MgO', 'C3H7NO2', 'Ni(NO3)2', 'Na2Cr2O7', 'C4H6O6', 'ZnI2', 'Br', 'AlBr3', 'C2H6Na4O12', 'C4H6O4Ni', 'Na2S2O3', 'C2H4O', 'CuSO4', 'C6H14O6', 'CaCl2', 'C5H8NO4Na', '(C8H8)n', 'CaC2', 'C2Cl4', 'NaClO3', 'KIO3', 'Pb(C2H3O2)2', 'KSCN', 'C4H10', 'C12H22O11', 'C27H36N2O10', 'CH2O', 'HCOOH', 'SF6', 'PCl3', 'C2H6', 'N2O5', 'H3PO3', 'K4Fe(CN)6', 'XeF2', 'Br2', 'C6H5', 'PI3', 'H2S2O8', 'K2HPO4', 'Al(OH)3', '(NH4)2S2O8', 'Na2[B4O5(OH)4]·8H2O', 'C2H3O2Cl', 'CH3CO2K', 'BaO', 'Cu2O', 'Cu(OH)2', 'SnO2', 'ClF3', 'C2H4', 'C2H2', 'Cr2O3', 'NaHSO4', 'CuCl2', 'HgCl2', 'SnCl2', 'C3H8', 'PbO2']

positive_charge = ["*+1", "*+2", "*+3", "*+4"]

negative_charge = ["*-1", "*-2", "*-3", "*-4"]

boyle = ["*P1", "*V1", "*P2", "*V2"]

charles = ["*T1", "*T2"]

avogadro = ["*N1", "*N2"]

ideal_gas = ["*p", "*V", "*n", "*R", "*T"]

combined_gas = ["*n1", "*P2", "*n2"]

constants = [
    "celcius_farenheit",
    "farenheit_celcius",
    "celcius_kelvin",
    "kelvin_celcius",
    "farenheit_kelvin",
    "kelvin_farenheit"
]
