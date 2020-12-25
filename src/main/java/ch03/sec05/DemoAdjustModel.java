/*
 * @author zYx.Tom
 * @email zhuyuanxiang@gmail.com
 * @date 2020-12-25 9:58
 */

package ch03.sec05;

import com.hankcs.hanlp.HanLP;
import com.hankcs.hanlp.dictionary.CoreDictionary;
import com.hankcs.hanlp.seg.Segment;

import static ch03.MSR.MSR_MODEL_PATH;
import static ch03.sec03.DemoNgramSegment.loadBigram;

/**
 * 《自然语言处理入门》
 * 3.5.3 调整模型
 */
public class DemoAdjustModel {
    public static void main(String[] args) {
        Segment segment = loadBigram(MSR_MODEL_PATH, false, false);
        assert CoreDictionary.contains("管道");
        String text = "北京输气管道工程";
        HanLP.Config.enableDebug();
        System.out.println(segment.seg(text));
    }
}
