import static java.util.Arrays.asList;
import io.IO;
import io.XMLRead;
import io.XMLWrite;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.FileWriter;
import java.io.InputStream;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.OutputStream;

import op.BFWalk;
import op.Operation;
import op.SimilarityMetrics;
import utils.Timer;
import data.Literal;
import data.Relation;
import data.RoWordNet;
import data.Synset;

/**
 * This class's purpose is to illustrate various ways the API can be used by
 * offering some usage examples.
 * 
 * @author Stefan Dumitrescu
 * @author Radu Petrut
 */
public class demo {

	public static void runDemos(String cuvant) throws Exception {


		Timer timer = new Timer();

		RoWordNet rown = RoWordNet.deserializeFromFile("RoWordNet\\res\\RoWordNet.data");


//		System.out.println("\n\n\n\nDemo 3: WordNet Breadth-First Walk\n------------------------------------------------------------------------\n");
		demo_bfWalk(rown, cuvant);

//		System.out.println("\n\n Demos have completed successfuly.");
	}

	/**
	 * Method that illustrates how the basic data structures and their
	 * associated operations work.
	 * 
	 * @param RoWordNet_XMLFilePath
	 *            the path where the dictionary is located on disk, under the
	 *            form of an XML file
	 * @throws Exception
	 */
	


	/**
	 * Demo of BFWalk on the RoWordNet semantic network
	 * 
	 * @param rown
	 *            input object
	 * @throws Exception
	 */
	private static void demo_bfWalk(RoWordNet rown, String cuvant) throws Exception {

		try
		{
			Synset source = rown.getSynsetsFromLiteral(new Literal(cuvant)).get(0);
			if (source == null)
				throw new Exception("Synset not found!");
			BFWalk bf = new BFWalk(rown, source.getId());
	
			int cnt = 0;
			
			while (bf.hasMoreSynsets()) {
	
				cnt = cnt +1;
				Synset step = rown.getSynsetById(bf.nextSynset());
	
				ArrayList<Literal> literali;
				
				literali = step.getLiterals();
				Iterator<Literal> iterator = literali.iterator();
				
				while(iterator.hasNext()) 
				{
					   Literal item = iterator.next();
					   System.out.write(item.getLiteral().getBytes("UTF-16"));
					   System.out.write(" ".getBytes("UTF-16"));
				}
				
				if (cnt > 6) {
	//				System.out.println("\n Stopping BFWalk and returning.");
	
					break;
				}
	
			}
		}
		catch(IndexOutOfBoundsException e){}
	}

}
