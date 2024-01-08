from pymol import cmd
import pandas as pd


from pymol import cmd
import glob

list_n = []
for name in glob.glob('/home/students/TP/Vincent_Rotation/AKT1/*.mol2'):
    li.append(name)

for i in list_n:
    cmd.load(i, state=0)



# Adding hydrogen and removing solvent
cmd.h_add
cmd.remove("solvent")


# Creating objects of selections of donors and acceptors
cmd.create("A", "elem O,F or (elem N and not (neighbor hydro) and not (fc. > 0))")
cmd.create("D", "(elem O + elem N + elem S) and (neighbor hydrogens)")


# One dictionary containing all the atoms to go through later
dict_ligands = {"don":[], "acc":[], "query":[]}


# Iterating each objects
cmd.iterate('D', "don.append('/%s/%s/%s/%s`%s/%s' % (model ,segi, chain, resn, resi, name))", space=dict_ligands)
cmd.iterate('A', "acc.append('/%s/%s/%s/%s`%s/%s' % (model ,segi, chain, resn, resi, name))", space=dict_ligands)


# Loading the pharmacohore
ph_name = "ppara_bbr_3CFF_query.pdb"
cmd.load("/home/students/TP/Vincent_Rotation/PPARA/ppara_bbr_3CFF_query.pdb", "ppara")
cmd.iterate("ppara", "query.append('/%s/%s/%s/%s`%s/%s' % (model ,segi, chain, resn, resi, name))", space=dict_ligands)


# Cut-off distances(values)??
# Functions to measure distances
def dist_D(atom_A):
    i = 0
    for b in dict_ligands["don"]:
        dist = cmd.get_distance(b, atom_A)
        if dis <= 2:
            i += 1
    return i
    
def dist_A(atom_D):
    ii = 0
    for bb in dict_ligands["acc"]:
        dist = cmd.get_distance(bb, atom_D)
        if dis <= 2:
            ii += 1
    return ii
   
def dist_G(atom_G):
    cmd.create("Hydropho", f"((elem C and not (neighbor elem N) and not (neighbor elem O) and not (neighbor elem F) and not A and not D and not ppara)) within 3 of ({atom_G})")
    temp={"gr":[]}
    cmd.iterate("Hydropho", "gr.append('%s' % (name))", space=temp)
    cmd.delete("Hydropho")
    if len(temp["gr"]) >= 1:
        return len(temp["gr"])
    else:
        return False
    

#Making all the data for query atoms in one single list(QAs)
QAs = []
# "at" is just an string.
for at in dict_ligands["query"]:
    l = []
    if at[8]=="A":
        l.append("Acceptor")
        l.append(at)
        l.append(dist_A(at))
        l.append(dist_D(at))
        l.append("NA")
        QAs.append(l)
    elif at[8]=="D":
        l.append("Donor")
        l.append(at)
        l.append(dist_A(at))
        l.append(dist_D(at))
        l.append("NA")
        QAs.append(l)
    elif at[8]=="B":
        if at[-1]=="O":
            l.append("Donor")
            l.append(at)
            l.append(dist_A(at))
            l.append(dist_D(at))
            l.append("NA")
            QAs.append(l)
        else:
            l.append("Acceptor")
            l.append(at)
            l.append(dist_A(at))
            l.append(dist_D(at))
            l.append("NA")
            QAs.append(l)
    elif at[8]=="G":
        l.append("Grease")
        l.append(at)
        l.append("NA")
        l.append("NA")
        l.append(dist_G(at))
        QAs.append(l)


table_labels = ["Label", "Atom's specs", "Acceptors for H-bonding", "Donors for H-bonding", "Hydrophobic interactions"]
table_index = []
for num in range(1, len(dict_ligands["query"])+1):
    table_index.append(f"{ph_name[0:4].capitalize()}_atom_{num}")


df = pd.DataFrame(data= QAs, index = table_index, columns = table_labels)

df.to_csv("PPARA.csv")
