/*
 * @author zYx.Tom
 * @email zhuyuanxiang@gmail.com
 * @date 2020-12-24 18:34
 */

package ch03;

import static tools.Tools.*;

/**
 * 《自然语言处理入门》
 */
public class MSR {
    public static final String MSR_GOLD_PATH = icwb2_data_path() + "gold/msr_test_gold.utf8";
    public static final String MSR_MODEL_PATH = test_data_path() + "msr_cws";
    public static final String MSR_OUTPUT_PATH = icwb2_data_path() + "testing/msr_output.txt";
    public static final String MSR_TEST_PATH = icwb2_data_path() + "testing/msr_test.utf8";
    public static final String MSR_TRAIN_PATH = icwb2_data_path() + "training/msr_training.utf8";
    public static final String MSR_TRAIN_WORDS = icwb2_data_path() + "gold/msr_training_words.utf8";
    public static final String MY_CWS_CORPUS_PATH = test_data_path() + "my_cws_corpus.txt";
    public static final String MY_MODEL_PATH = get_root_path() + "data/model/my_cws_model";
}
