package literateProgramming;

import java.io.File;

import consts.PathConstanct;
import utils.StanfordLemmatizer;

public class TokensExtractionFromLPCodeTree {
//	public static String[] arrLibraryPrefix={"android","com.google.gwt","com.thoughtworks.xstream","org.hibernate","org.joda.time","java"};
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String inPath=constanct.PathConstanct.PathLiterateProgrammingExpReplication+"IVC"+File.separator+"b_code-missingMIs"+File.separator;
		String outPath=constanct.PathConstanct.PathLiterateProgrammingExpReplication+File.separator+"step0_sequence"+File.separator;
		StanfordLemmatizer lemm=new StanfordLemmatizer();
		OnlySourceSequenceGeneratorForNL mcsg=new OnlySourceSequenceGeneratorForNL(inPath,lemm);
		mcsg.generateSequences(outPath);
	}

}
