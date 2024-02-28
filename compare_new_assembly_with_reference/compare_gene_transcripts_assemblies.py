from pygtftk.gtf_interface import GTF
import sys



#select all transcript and exon entries from custom2 gtf and write to a new gtf file
def main():
    def get_transcript_string(transcript_ids) -> str:
        '''get string of transcript or other ids for filtering 
        of a GTF class object from pygtftk'''
        transcript_string = ''
        for transcript_id in transcript_ids[:-1]:
            transcript_string += transcript_id+','
        transcript_string += transcript_ids[-1]
        return transcript_string
    
    
    custom_gtf = GTF(sys.argv[1], check_ensembl_format=False)
    custom2_gtf = GTF(sys.argv[2], check_ensembl_format=False)
    custom_transcript_ids = set(custom_gtf.get_tx_ids(nr=True))
    custom2_transcript_ids = set(custom2_gtf.get_tx_ids(nr=True))
    custom_gene_ids = set(custom_gtf.get_gn_ids(nr=True))
    custom2_gene_ids = set(custom2_gtf.get_gn_ids(nr=True))

    custom_gene_ids_MSTRG = [gene for gene in custom_gene_ids if gene.startswith('MSTRG')]
    custom2_gene_ids_MSTRG = [gene for gene in custom2_gene_ids if gene.startswith('MSTRG')]

    
    custom_MSTRG_gene_string = get_transcript_string(custom_gene_ids_MSTRG)
    custom2_MSTRG_gene_string = get_transcript_string(custom2_gene_ids_MSTRG)

    MSTRG_genes_transcirpts_custom1 = custom_gtf.select_by_key('feature', 'transcript')\
    .select_by_key('gene_id', custom_MSTRG_gene_string)
    MSTRG_genes_transcirpts_custom2 = custom2_gtf.select_by_key('feature', 'transcript')\
    .select_by_key('gene_id', custom2_MSTRG_gene_string)
    MSTRG_tid_custom = set(MSTRG_genes_transcirpts_custom1.get_tx_ids(nr=True))
    MSTRG_tid_custom2 = set(MSTRG_genes_transcirpts_custom2.get_tx_ids(nr=True))
    


    intersection_tid = [tid for tid in custom2_transcript_ids if tid in custom_transcript_ids]
    only_custom_tid = [tid for tid in custom_transcript_ids if tid not in custom2_transcript_ids]
    only_custom2_tid = [tid for tid in custom2_transcript_ids if tid not in custom_transcript_ids]

    print('intersection tids', len(intersection_tid))
    print(f'only {sys.argv[1]} tids', len(only_custom_tid))
    print(f'{sys.argv[1]} of which MSTRG transcripts', len(set(t for t in only_custom_tid if t.startswith('MSTRG'))), '\n')
    print(f'only {sys.argv[2]} tids', len(only_custom2_tid))
    print(f'{sys.argv[2]}  of which MSTRG transcripts', len(set(t for t in only_custom2_tid if t.startswith('MSTRG'))))
    f = open(sys.argv[3], 'w')
    f.write('\n'.join(str(item) for item in only_custom_tid))
    f.close()

    f = open(sys.argv[4], 'w')
    f.write('\n'.join(str(item) for item in only_custom2_tid))
    f.close()


    intersection_gid = [gid for gid in custom2_gene_ids if gid in custom_gene_ids]
    only_custom_gid = [gid for gid in custom_gene_ids if gid not in custom2_gene_ids]
    only_custom2_gid = [gid for gid in custom2_gene_ids if gid not in custom_gene_ids]

    print('intersection gids', len(intersection_gid))
    print(f'only {sys.argv[1]} gids', len(only_custom_gid))
    print(f'only {sys.argv[2]} gids', len(only_custom2_gid))
    f = open(sys.argv[5], 'w')
    f.write('\n'.join(str(item) for item in only_custom_gid))
    f.close()

    f = open(sys.argv[6], 'w')
    f.write('\n'.join(str(item) for item in only_custom2_gid))
    f.close()


    #write intersection files
    f = open(sys.argv[7], 'w')
    f.write('\n'.join(str(item) for item in intersection_tid))
    f.close()

    f = open(sys.argv[8], 'w')
    f.write('\n'.join(str(item) for item in intersection_gid))
    f.close()


    print(f'{sys.argv[1]} nr transcripts of MSTRG genes', len(MSTRG_tid_custom))
    print(f'{sys.argv[2]}  nr transcripts of MSTRG genes', len(MSTRG_tid_custom2))
    
    
    
    

if __name__ == '__main__':
    main()




   