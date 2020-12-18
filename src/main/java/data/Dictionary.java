package data;

import com.hankcs.hanlp.corpus.io.IOUtil;
import com.hankcs.hanlp.dictionary.CoreDictionary;

import java.io.IOException;
import java.util.TreeMap;

public class Dictionary {
    public static TreeMap<String, CoreDictionary.Attribute> loadDictionary(int minLength) throws IOException {
        TreeMap<String, CoreDictionary.Attribute> dictionary =
                IOUtil.loadDictionary("data/dictionary/CoreNatureDictionary.mini.txt");
        if (minLength > 0)
            dictionary.keySet().removeIf(s -> s.length() < minLength);
        return dictionary;
    }
}
