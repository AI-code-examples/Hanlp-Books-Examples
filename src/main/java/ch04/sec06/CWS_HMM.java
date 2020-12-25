/*
 * @author zYx.Tom
 * @email zhuyuanxiang@gmail.com
 * @date 2020-12-25 15:05
 */

package ch04.sec06;

import com.hankcs.hanlp.model.hmm.FirstOrderHiddenMarkovModel;
import com.hankcs.hanlp.model.hmm.HMMSegmenter;
import com.hankcs.hanlp.model.hmm.HiddenMarkovModel;
import com.hankcs.hanlp.model.hmm.SecondOrderHiddenMarkovModel;
import com.hankcs.hanlp.seg.Segment;
import com.hankcs.hanlp.seg.common.CWSEvaluator;

import java.io.IOException;

import static ch03.MSR.*;

/**
 * 《自然语言处理入门》
 * 4.6 孢马尔可夫模型应用于中文分词
 */
public class CWS_HMM {
    public static void main(String[] args) throws IOException {
        trainAndEvaluate(new FirstOrderHiddenMarkovModel());
        trainAndEvaluate(new SecondOrderHiddenMarkovModel());
    }

    private static void trainAndEvaluate(HiddenMarkovModel model) throws IOException {
        Segment hmm = trainHMM(model);
        CWSEvaluator.Result result = CWSEvaluator.evaluate(hmm, MSR_TEST_PATH, MSR_OUTPUT_PATH, MSR_GOLD_PATH, MSR_TRAIN_WORDS);
        System.out.println(result);
    }

    private static Segment trainHMM(HiddenMarkovModel model) throws IOException {
        HMMSegmenter segmenter = new HMMSegmenter();
        segmenter.train(MSR_TRAIN_PATH);
        System.out.println(segmenter.segment("商品和服务"));
        return segmenter.toSegment();
    }
}
