package ch03.sec03;

import com.hankcs.hanlp.HanLP;
import com.hankcs.hanlp.corpus.dictionary.NatureDictionaryMaker;
import com.hankcs.hanlp.corpus.document.CorpusLoader;
import com.hankcs.hanlp.corpus.document.sentence.word.IWord;
import com.hankcs.hanlp.dictionary.CoreBiGramTableDictionary;
import com.hankcs.hanlp.dictionary.CoreDictionary;
import com.hankcs.hanlp.seg.Dijkstra.DijkstraSegment;
import com.hankcs.hanlp.seg.Segment;
import com.hankcs.hanlp.seg.Viterbi.ViterbiSegment;

import java.util.List;

import static ch03.MSR.*;
import static tools.Tools.show_subtitle;

public class DemoNgramSegment {

    public static void main(String[] args) {
        // 第一次执行会报出警告，然后会转换 txt 文件为 bin 文件，后面就不再报错
        // 连续执行两次时，第二次使用的是第一次载入的 bin 文件
        // 交换以下现场代码的顺序就可以看到区别
        show_subtitle("my_cws_model");
        trainBigram(MY_CWS_CORPUS_PATH, MY_MODEL_PATH);
        loadBigram(MY_MODEL_PATH);
        // ToDo: HanLP 更新了版本，增加了 CoreDictionary.reload() 函数，我还没有更新版本，没有测试这个功能。
        show_subtitle("msr_ngram");
        trainBigram(MSR_TRAIN_PATH, MSR_MODEL_PATH);
        loadBigram(MSR_MODEL_PATH);
    }

    /**
     * 训练 bigram 模型
     *
     * @param corpusPath 语料库路径
     * @param modelPath  模型保存路径
     */
    public static void trainBigram(String corpusPath, String modelPath) {
        List<List<IWord>> sentenceList = CorpusLoader.convert2SentenceList(corpusPath);
        for (List<IWord> sentence : sentenceList)
            for (IWord word : sentence)
                if (word.getLabel() == null) word.setLabel("n");  // 赋予每个单词一个虚拟的名词词性
        final NatureDictionaryMaker dictionaryMaker = new NatureDictionaryMaker();
        dictionaryMaker.compute(sentenceList);
        dictionaryMaker.saveTxtTo(modelPath);
    }

    public static Segment loadBigram(String modelPath) {
        return loadBigram(modelPath, true, true);
    }

    private static Segment loadBigram(String modelPath, boolean verbose, boolean viterbi) {
//        HanLP.Config.enableDebug();
        HanLP.Config.CoreDictionaryPath = modelPath + ".txt";
        HanLP.Config.BiGramDictionaryPath = modelPath + ".ngram.txt";
        if (verbose) {
            HanLP.Config.ShowTermNature = false;
            System.out.println("「商品」的词频：" + CoreDictionary.getTermFrequency("商品"));
            System.out.println("「商品@和」的频次：" + CoreBiGramTableDictionary.getBiFrequency("商品", "和"));
            Segment segment = new DijkstraSegment()
                    .enableAllNamedEntityRecognize(false)   // 禁用命名实体识别
                    .enableCustomDictionary(false);         // 禁用用户词典
            System.out.println(segment.seg("商品和服务"));
            System.out.println(segment.seg("货币和服务"));
        }
        Segment viterbiSegment = new ViterbiSegment().enableAllNamedEntityRecognize(false).enableCustomDictionary(false);
        Segment dijkstraSegment = new DijkstraSegment().enableAllNamedEntityRecognize(false).enableCustomDictionary(false);
        return viterbi ? viterbiSegment : dijkstraSegment;
    }
}
