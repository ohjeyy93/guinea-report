params.gpm1 = "$baseDir/Gp1_pooled_merge_final.csv"
params.gpm2 = "$baseDir/GP2_merge_final.csv"
params.gpm11 = "$baseDir/Gp1_pooled_merge_final.csv"
params.gpm22 = "$baseDir/GP2_merge_final.csv"
params.gpi1 = "$baseDir/gp1_paired_merge.csv"
params.p1 = "$baseDir/Pooled_Info_Part1.csv"
params.p2 = "$baseDir/Pooled_Info_Part2_fixed.csv"
params.p11 = "$baseDir/Pooled_Info_Part1.csv"
params.p22 = "$baseDir/Pooled_Info_Part2_fixed.csv"
params.i1 = "$baseDir/Paired_Info.csv"
params.voi1 = "$baseDir/voinew3.csv"
params.voi2 = "$baseDir/voinew3.csv"
params.voi3 = "$baseDir/voinew3.csv"


process merge_individual {
    publishDir "$params.output.folder/individual/", pattern: "*.csv", mode : "copy"
    input:
        path i1 from params.i1
        path voi from params.voi1
        path gpi from params.gpi1

    output:
        path("gp1_paired_merge_fl.csv") into fl_ind_out1
        path("gp1_paired_merge_df.csv") into df_ind_out2

    script:
        """
        python $baseDir/pyscripts/mergegn_by_forloops_ind.py -v ${voi} -g ${gpi} -p ${i1}
        python $baseDir/pyscripts/mergegn_by_dataframes_ind.py -v ${voi} -g ${gpi} -p ${i1}
        """
}

process merge_pooled_fl {
    publishDir "$params.output.folder/pooled_fl/", pattern: "*.csv", mode : "copy"
    input:
        path pfl1 from params.p1
        path voifl from params.voi2
        path gpmfl2 from params.gpm2
        path gpmfl1 from params.gpm1
        path pfl2 from params.p2

    output:
        path("Gp1_pooled_merge_final_fl_p2.csv") into fl_p1_out1
        path("Gp2_pooled_merge_final_fl_p1.csv") into fl_p2_out2

    script:
        """
        python $baseDir/pyscripts/mergegn_by_forloops_p1.py -v ${voifl} -g ${gpmfl2} -p ${pfl1}
        python $baseDir/pyscripts/mergegn_by_forloops_p2.py -v ${voifl} -g ${gpmfl1} -p ${pfl2}
        """
}

process merge_pooled_df {
    publishDir "$params.output.folder/pooled_df/", pattern: "*.csv", mode : "copy"
    input:
        path pdf1 from params.p11
        path voidf from params.voi3
        path gpmdf2 from params.gpm22
        path gpmdf1 from params.gpm11
        path pdf2 from params.p22

    output:
        path("GP2_merge_final_df_p1.csv") into df_p1_out1
        path("Gp1_pooled_merge_final_df_p2.csv") into df_p2_out2

    script:
        """
        python $baseDir/pyscripts/mergegn_by_dataframes_p1.py -v ${voidf} -g ${gpmdf2} -p ${pdf1}
        python $baseDir/pyscripts/mergegn_by_dataframes_p2.py -v ${voidf} -g ${gpmdf1} -p ${pdf2}
        """
}

process stack_gps {
    publishDir "$params.output.folder/stacked/", pattern: "*.csv", mode : "copy"
    input:
        path(gp1fl) from fl_p1_out1
        path(gp2fl) from fl_p2_out2
        path(gp2df) from df_p1_out1
        path(gp1df) from df_p2_out2

    output:
        path("GP_merge_stacked_final_df.csv") into df_stack_out1
        path("GP_merge_stacked_final_fl.csv") into fl_stack_out1

    script:
        """
        python $baseDir/pyscripts/stack2.py -g1 ${gp1fl} -g2 ${gp2fl} -o GP_merge_stacked_final_fl.csv
        python $baseDir/pyscripts/stack2.py -g1 ${gp1df} -g2 ${gp2df} -o GP_merge_stacked_final_df.csv
        """
}

process reorganize {
    publishDir "$params.output.folder/organized/", pattern: "*.csv", mode : "copy"
    input:
        path(gpstackdf) from df_stack_out1
        path(gpstackfl) from fl_stack_out1

    output:
        path("pooled_seq_results_fl_re1.csv") into fl_organize_out1
        path("pooled_seq_results_df_re1.csv") into df_organize_out1

    script:
        """
        python $baseDir/pyscripts/reorganize.py -s ${gpstackfl} -r pooled_seq_results_fl_re1.csv 
        python $baseDir/pyscripts/reorganize.py -s ${gpstackdf} -r pooled_seq_results_df_re1.csv
        """
}

process weight {
    publishDir "$params.output.folder/weight/", pattern: "*.csv", mode : "copy"
    input:
        path(organized1) from fl_organize_out1
        path(individualfl) from fl_ind_out1
        path(organized2) from df_organize_out1
        path(individualdf) from df_ind_out2

    output:
        path("weight_fl.csv") into fl_weight_out1
        path("weight_df.csv") into df_weight_out1

    script:
        """
        python $baseDir/pyscripts/weight.py -i ${individualfl} -p ${organized1} -o weight_fl.csv
        python $baseDir/pyscripts/weight.py -i ${individualdf} -p ${organized2} -o weight_df.csv
        """
}

process weightextra {
    publishDir "$params.output.folder/weightextra/", pattern: "*.csv", mode : "copy"
    input:
        path(weightfl) from fl_weight_out1
        path(weightdf) from df_weight_out1

    output:
        path("weight_fl_extra.csv") into fl_weight_extra_out1
        path("weight_df_extra.csv") into df_weight_extra_out1

    script:
        """
        python $baseDir/pyscripts/extra.py -i ${weightfl} -o weight_fl_extra.csv
        python $baseDir/pyscripts/extra.py -i ${weightdf} -o weight_df_extra.csv
        """
}