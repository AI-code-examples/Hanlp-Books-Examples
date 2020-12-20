package ch02.sec09;


import com.hankcs.hanlp.seg.Other.DoubleArrayTrieSegment;
import com.hankcs.hanlp.seg.Segment;
import com.hankcs.hanlp.seg.common.CWSEvaluator;

import java.io.IOException;

import static tools.Tools.get_root_path;

public class EvaluateCWS {
    public static void main(String[] args) throws IOException {
        String root_path=get_root_path();
        String msr_dict = root_path + "/data/test/icwb2-data/gold/msr_training_words.utf8";
        String msr_test = root_path + "/data/test/icwb2-data/testing/msr_test.utf8";
        String msr_output = root_path + "/data/test/icwb2-data/testing/msr_output.txt";
        String msr_gold = root_path + "/data/test/icwb2-data/gold/msr_test_gold.utf8";
        Segment segment=new DoubleArrayTrieSegment(msr_dict).enablePartOfSpeechTagging(true);
        CWSEvaluator.Result result=CWSEvaluator.evaluate(segment,msr_test,msr_output,msr_gold,msr_dict);
        System.out.println(result);
    }
}
