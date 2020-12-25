package ch03.sec03;

import com.hankcs.hanlp.corpus.document.CorpusLoader;
import com.hankcs.hanlp.corpus.document.sentence.word.IWord;
import com.hankcs.hanlp.corpus.io.IOUtil;

import java.util.List;

import static ch03.MSR.MY_CWS_CORPUS_PATH;

/**
 * 手工加载语料库
 */
public class DemoCorpusLoader {
    static {
        if (!IOUtil.isFileExisted(MY_CWS_CORPUS_PATH))
            IOUtil.saveTxt(MY_CWS_CORPUS_PATH, "商品 和 服务\n" + "商品 和服 物美价廉\n" + "服务 和 货币");
    }

    public static void main(String[] args) {
        List<List<IWord>> sentenceList = CorpusLoader.convert2SentenceList(MY_CWS_CORPUS_PATH);
        for (List<IWord> sentence : sentenceList) {
            System.out.println("sentence: " + sentence);
            System.out.print("word: ");
            for (IWord word : sentence)
                System.out.print(word + ", ");
            System.out.println();
        }
    }
}
