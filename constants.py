digits = "0123456789"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
    "||": "OR",
    "==>" : "BALANCINGARROW"
}

assignments = {
    "=" : "ASSIGN",
    "+=" : "ADDASSIGN",
    "-=" : "SUBTRACTASSIGN",
    "*=" : "MULTIPLYASSIGN",
    "/=" : "DIVIDEASSIGN",
    "%=" : "MODULOASSIGN"
}

keywords = [
    "assuming",
    "break",
    "class",
    "continue",
    "def",
    "except",
    "import",
    "in",
    "inp",
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
    "@": "ATSIGN", # di pa ata nadadagdag sa documentation
    "\\" : "BACKSLASH",
    "_": "UNDERSCORE",
    '"' : "QUOTATIONMARK",
    "'" : "APOSTROPHE",
    "?" : "QUESTIONMARK",
    "{" : "LEFTCURLYBRACE",
    "}" : "RIGHTCURLYBRACE",
    "(" : "LEFTROUNDBRACKET",
    ")" : "RIGHTROUNDBRACKET", #consider in int
    "[" : "LEFTSQUAREBRACKET",
    "]" : "RIGHTSQUAREBRACKET",# consider in int
    "`" : "BACKTICK"
}

comments = {
    "//" : "COMMENT",
    "#" : "MULTILINECOMMENT"
}

delimeters = {
    ";" : "SEMICOLON",
    "," : "COMMA",
    ".": "PERIOD"
}

booleans = {
    "true",
    "false"
}

at_num = ["@1", "@2", "@3", "@4", "@5", "@6", "@7", "@8", "@9", "@10", "@11", "@12", "@13", "@14", "@15", "@16", "@17", "@18", "@19", "@20", "@21", "@22", "@23", "@24", "@25", "@26", "@27", "@28", "@29", "@30", "@31", "@32", "@33", "@34", "@35", "@36", "@37", "@38", "@39", "@40", "@41", "@42", "@43", "@44", "@45", "@46", "@47", "@48", "@49", "@50", "@51", "@52", "@53", "@54", "@55", "@56", "@57", "@58", "@59", "@60", "@61", "@62", "@63", "@64", "@65", "@66", "@67", "@68", "@69", "@70", "@71", "@72", "@73", "@74", "@75", "@76", "@77", "@78", "@79", "@80", "@81", "@82", "@83", "@84", "@85", "@86", "@87", "@88", "@89", "@90", "@91", "@92", "@93", "@94", "@95", "@96", "@97", "@98", "@99", "@100", "@101", "@102", "@103", "@104", "@105", "@106", "@107", "@108", "@109", "@110", "@111", "@112", "@113", "@114", "@115", "@116", "@117", "@118"]

# 1st Group in identifying the symbol of the elements.
metals = ["Li", "Na", "K", "Rb", "Cs", "Fr", "Be", "Mg", "Ca", "Sr", "Ba", "Ra", "Al", "Ga", "In", "Tl", "Sn", "Pb", "Bi", "Po"]
non_metals = ["H", "C", "N", "P", "O", "S", "Se", "F", "Cl", "Br", "I", "At", "He", "Ne", "Ar", "Kr", "Xe", "Rn"]
metalloids = ["B", "Si", "Ge", "As", "Sb", "Te", "Po"]

# 1st Group in classifying the element name
n_metals = ["Lithium", "Sodium", "Potassium", "Rubidium", "Cesium", "Francium", "Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium", "Aluminum", "Gallium", "Indium", "Thallium", "Tin", "Lead", "Bismuth", "Polonium"]
n_non_metals = ["Hydrogen", "Carbon", "Nitrogen", "Phosphorus", "Oxygen", "Sulfur", "Selenium", "Fluorine", "Chlorine", "Bromine", "Iodine", "Astatine", "Helium", "Neon", "Argon", "Krypton", "Xenon", "Radon"]
n_metalloids = ["Boron", "Silicon", "Germanium", "Arsenic", "Antimony", "Tellurium", "Polonium"]


# 2nd Group in identifying the symbol of the elements.
alkali_list = ["@H", "@Li", "@Na", "@K", "@Rb", "@Cs", "@Fr"]
alkaline_earth_list = ["@Be", "@Mg", "@Ca", "@Sr", "@Ba", "@Ra"]
icosagens_list = ["@B", "@Al", "@Ga", "@In", "@Tl"]
crystal_list = ["@C", "@Si", "@Ge", "@Sn", "@Pb"]
pnicto_list = ["@N", "@P", "@As", "@Sb", "@Bi"]
chalco_list = ["@O", "@S", "@Se", "@Te", "@Po"]
halo_list = ["@F", "@Cl", "@Br", "@I", "@At"]
noble_list = ["@He", "@Ne", "@Ar", "@Kr", "@Xe", "@Rn"]


# 2nd Group in identifying the element name.
n_alkali_list = ["@Hydrogen", "@Lithium", "@Sodium", "@Potassium", "@Rubidium", "@Cesium", "@Francium"]
n_alkaline_earth_list = ["@Beryllium", "@Magnesium", "@Calcium", "@Strontium", "@Barium", "@Radium"]
n_icosagens_list = ["@Boron", "@Aluminum", "@Gallium", "@Indium", "@Thallium"]
n_crystal_list = ["@Carbon", "@Silicon", "@Germanium", "@Tin", "@Lead"]
n_pnicto_list = ["@Nitrogen", "@Phosphorus", "@Arsenic", "@Antimony", "@Bismuth"]
n_chalco_list = ["@Oxygen", "@Sulfur", "@Selenium", "@Tellurium", "@Polonium"]
n_halo_list = ["@Fluorine", "@Chlorine", "@Bromine", "@Iodine", "@Astatine"]
n_noble_list = ["@Helium", "@Neon", "@Argon", "@Krypton", "@Xenon", "@Radon"]


constants = [
    "celcius_farenheit",
    "farenheit_celcius",
    "celcius_kelvin",
    "kelvin_celcius",
    "farenheit_kelvin",
    "kelvin_farenheit",
    "at_num",
    "metals",
    "non_metals",
    "metalloids",
    "n_metals",
    "n_non_metals",
    "n_metalloids",
    "alkali_list",
    "alkaline_earth_list",
    "icosagens_list",
    "crystal_list ",
    "pnicto_list",
    "chalco_list",
    "halo_list",
    "noble_list",
    "n_alkali_list",
    "n_alkaline_earth_list",
    "n_icosagens_list",
    "n_crystal_list",
    "n_pnicto_list",
    "n_chalco_list",
    "n_halo_list",
    "n_noble_list",
    "pos_charges",
    "neg_charges",
    "at_charges",
    "grp1_sym",
    "grp1_name",
    "grp1",
    "grp2_sym",
    "grp2_name",
    "grp2",
    "atomic_element",
    "gas_laws",
    "boyle",
    "charles",
    "gay_lussac",
    "avogadro",
    "ideal_gas",
    "combined_gas"
]
