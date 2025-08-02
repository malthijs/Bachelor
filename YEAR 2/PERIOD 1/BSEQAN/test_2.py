from BCBio import GFF

in_file = "your_file.gff"

in_handle = open(in_file)
for rec in GFF.parse(in_handle):
    print(rec)
in_handle.close()
