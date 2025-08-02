"""
TEST
"""


from re import split as regex_split


def chromosome_or_plasmid() -> list[str]:
    """
    :return:
    """
    with open("hollandica.gff", encoding="UTF-8") as f:
        gff = f.read()
        gff = regex_split(r"##.*", gff)

        gff_data_chromosome = []
        gff_data_plasmid = []
        garbage = []
        for index, item in enumerate(gff):
            if item.find("genome=chromosome") != -1:
                gff_data_chromosome.append(item.strip("\n"))
            if item.find("genome=plasmid") != -1:
                gff_data_plasmid.append(item.strip("\n"))
            else:
                garbage.append(item.strip("\n"))
    print(f"{gff_data_plasmid}")
    return gff_data_plasmid


def parser(data_plasmid: list[str]) -> list[str]:
    """
    :return:
    """
    data_genes = []

    return data_genes


def main():
    """
    :return:
    """
    data_plasmid = chromosome_or_plasmid()
    data_genes = parser(data_plasmid)


if __name__ == '__main__':
    main()
