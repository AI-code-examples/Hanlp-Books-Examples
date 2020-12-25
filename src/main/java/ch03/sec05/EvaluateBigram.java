/*
 * @author zYx.Tom
 * @email zhuyuanxiang@gmail.com
 * @date 2020-12-24 18:31
 */

package ch03.sec05;

import com.hankcs.hanlp.seg.Segment;
import com.hankcs.hanlp.seg.common.CWSEvaluator;

import java.io.IOException;

import static ch03.MSR.*;
import static ch03.sec03.DemoNgramSegment.loadBigram;
import static ch03.sec03.DemoNgramSegment.trainBigram;
import static com.hankcs.hanlp.seg.common.CWSEvaluator.evaluate;


/**
 * 《自然语言处理入门》 3.5 评测
 * 二元语法训练模型
 */
public class EvaluateBigram {
    public static void main(String[] args) throws IOException {
        // Note: MSR 无法从 com.hankcs.hanlp.corpus.MSR 中导入
        trainBigram(MSR_TRAIN_PATH, MSR_MODEL_PATH);
        Segment segment = loadBigram(MSR_MODEL_PATH);
        CWSEvaluator.Result result = evaluate(segment, MSR_TEST_PATH, MSR_OUTPUT_PATH, MSR_GOLD_PATH, MSR_TRAIN_WORDS);
        System.out.println(result);
    }
}
