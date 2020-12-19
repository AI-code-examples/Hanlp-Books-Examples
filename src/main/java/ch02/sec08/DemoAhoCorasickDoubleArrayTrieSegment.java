package ch02.sec08;

import com.hankcs.hanlp.HanLP;
import com.hankcs.hanlp.seg.Other.AhoCorasickDoubleArrayTrieSegment;

import java.io.IOException;

public class DemoAhoCorasickDoubleArrayTrieSegment {
    public static void main(String[] args) throws IOException {
        HanLP.Config.ShowTermNature=false;
        AhoCorasickDoubleArrayTrieSegment segment=new AhoCorasickDoubleArrayTrieSegment();
        System.out.println(segment.seg("江西鄱阳湖干枯，中国最大淡水湖变成大草原"));
    }
}
