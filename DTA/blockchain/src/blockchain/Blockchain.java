package blockchain;
import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import java.io.*;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.Date;
import java.util.LinkedHashMap;

public class Blockchain {
    private ArrayList<Block> blockchain;
    private int numOfBlock;
    private ListOfUsers listOfUsers;
    private LinkedHashMap<String, String> files;

    public Blockchain() throws NoSuchAlgorithmException, FileNotFoundException {
//        this.blockchain = new ArrayList<>();
//        this.numOfBlock = 0;
//        ArrayList<Transaction> listOfTransactions = new ArrayList<>();
//        listOfTransactions.add(new Transaction("", "", 0));
//        mineAndAddBlock(listOfTransactions);
//        this.listOfUsers = new ListOfUsers();
//        this.files = new LinkedHashMap<>();
//        this.files.put("blockchain", "src/blockchain/blockchain2.yaml");
//        this.files.put("listOfUsers", "src/blockchain/listOfUsers2.yaml");
//        this.toYaml(this.files.get("blockchain"));
//        this.listOfUsers.toYaml(this.files.get("listOfUsers"));
    }
    public Blockchain(LinkedHashMap<String, String> files) throws FileNotFoundException {
        this.files = files;
        this.blockchain = new ArrayList<>();
        this.listOfUsers = new ListOfUsers();
        this.fromYaml(files.get("blockchain"));
        this.listOfUsers.fromYaml(files.get("listOfUsers"));
    }

    public ArrayList<Block> getBlockchain() {
        return this.blockchain;
    }
    public int getNumOfBlock() {
        return this.numOfBlock;
    }
    public ListOfUsers getListOfUsers() {
        return this.listOfUsers;
    }
    public LinkedHashMap<String, String> getFiles() {
        return this.files;
    }
    public void setBlockchain(ArrayList<Block> blockchain) {
        this.blockchain = blockchain;
    }
    public void setNumOfBlock(int numOfBlock) {
        this.numOfBlock = numOfBlock;
    }
    public void setListOfUsers(ListOfUsers listOfUsers) {
        this.listOfUsers = listOfUsers;
    }
    public void setFiles(LinkedHashMap<String, String> files) {
        this.files = files;
    }

    private void addBlock(Block block) {
        this.blockchain.add(block);
        this.numOfBlock++;
    }
    public void mineAndAddBlock(ArrayList<Transaction> listOfTransactions) throws NoSuchAlgorithmException {
        String previousHash;
        if (this.numOfBlock == 0)
            previousHash = "0";
        else
            previousHash = getBlockchain().get(this.numOfBlock - 1).getHash();
        StringBuilder stringOfTransactions = new StringBuilder();
        for (Transaction t : listOfTransactions) {
            stringOfTransactions.append(t.toString());
        }
        long dateOfCreation = new Date().getTime();
        String blockToString = previousHash + stringOfTransactions + dateOfCreation;

        int proof = 0;
        String input = blockToString + proof;
        String hash = Hash.calculateHash(input);

        while (!hash.startsWith("000000")) {
            proof++;
            input = blockToString + proof;
            hash = Hash.calculateHash(input);
        }
        Block block = new Block(previousHash, listOfTransactions, dateOfCreation, proof, hash);
        addBlock(block);
    }
    public void toYaml(String path) throws FileNotFoundException {
        DumperOptions options = new DumperOptions();
        options.setIndent(2);
        options.setPrettyFlow(true);
        options.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);

        Yaml yamlFile = new Yaml(options);
        LinkedHashMap<String, Object> map = new LinkedHashMap<>();
        ArrayList<LinkedHashMap<String, Object>> mapBlocks = new ArrayList<>();

        this.blockchain.forEach(block -> mapBlocks.add(block.toLinkedHashMap()));

        map.put("blockchain", mapBlocks);
        map.put("numOfBlock", this.numOfBlock);
        map.put("files", this.files);

        PrintWriter doc = new PrintWriter(new File(path));
        yamlFile.dump(map, doc);
    }
    public void fromYaml(String path) throws FileNotFoundException {
        this.blockchain.clear();
        Yaml yaml = new Yaml(new Constructor(Blockchain.class));
        InputStream inputStream = new FileInputStream(path);
        Blockchain bc = yaml.load(inputStream);
        this.blockchain = bc.blockchain;
        this.numOfBlock = bc.numOfBlock;
        this.files = bc.files;
    }
}