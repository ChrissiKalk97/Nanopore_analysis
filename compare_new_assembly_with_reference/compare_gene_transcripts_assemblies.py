from pygtftk.gtf_interface import GTF
import sys



#select all transcript and exon entries from ensembl gtf and write to a new gtf file
def main():
    ensembl_gtf = GTF(sys.argv[1], check_ensembl_format=False)
    custom_gtf = GTF(sys.argv[2], check_ensembl_format=False)
    custom_transcript_ids = set(custom_gtf.get_tx_ids(nr=True))
    ensembl_transcript_ids = set(ensembl_gtf.get_tx_ids(nr=True))
    custom_gene_ids = set(custom_gtf.get_gn_ids(nr=True))
    ensembl_gene_ids = set(ensembl_gtf.get_gn_ids(nr=True))

    intersection_tid = [tid for tid in ensembl_transcript_ids if tid in custom_transcript_ids]
    only_custom_tid = [tid for tid in custom_transcript_ids if tid not in ensembl_transcript_ids]
    only_ensembl_tid = [tid for tid in ensembl_transcript_ids if tid not in custom_transcript_ids]

    print("intersection tids", len(intersection_tid))
    print("only new assembly tids", len(only_custom_tid))
    print("only ensmebl tids", len(only_ensembl_tid))
    f = open(sys.argv[3], "w")
    f.write("\n".join(str(item) for item in only_custom_tid))
    f.close()

    f = open(sys.argv[4], "w")
    f.write("\n".join(str(item) for item in only_ensembl_tid))
    f.close()


    intersection_gid = [gid for gid in ensembl_gene_ids if gid in custom_gene_ids]
    only_custom_gid = [gid for gid in custom_gene_ids if gid not in ensembl_gene_ids]
    only_ensembl_gid = [gid for gid in ensembl_gene_ids if gid not in custom_gene_ids]

    print("intersection gids", len(intersection_gid))
    print("only new assembly gids", len(only_custom_gid))
    print("only ensmebl gids", len(only_ensembl_gid))
    f = open(sys.argv[5], "w")
    f.write("\n".join(str(item) for item in only_custom_gid))
    f.close()

    f = open(sys.argv[6], "w")
    f.write("\n".join(str(item) for item in only_ensembl_gid))
    f.close()


    #write intersection files
    f = open(sys.argv[7], "w")
    f.write("\n".join(str(item) for item in intersection_tid))
    f.close()

    f = open(sys.argv[8], "w")
    f.write("\n".join(str(item) for item in intersection_gid))
    f.close()

if __name__ == "__main__":
    main()




   