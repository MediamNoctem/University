package blockchain;
import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import java.io.*;
import java.security.NoSuchAlgorithmException;
import java.util.*;

public class Blockchain {
    private ArrayList<Block> blockchain;
    private int numOfBlocks;
    private ArrayList<Transaction> pool; // Список транзакций, не добавленных в предыдущие блоки.
    private ListOfUsers listOfUsers;
    private LinkedHashMap<String, String> files;

    public Blockchain() {}
    public Blockchain(LinkedHashMap<String, String> files) throws IOException, NoSuchAlgorithmException {
        this.files = files;
        this.blockchain = new ArrayList<>();
        this.pool = new ArrayList<>();
        this.listOfUsers = new ListOfUsers();
        File file = new File(this.files.get("blockchain"));
        if (file.createNewFile()) {
            this.numOfBlocks = 0;
            this.pool.add(new Transaction("", "", 0));
            Block genesisBlock = mineBlock();
            this.addBlock(genesisBlock);
            this.toYaml(files.get("blockchain"));
        }
        else
            this.fromYaml(files.get("blockchain"));
        file = new File(this.files.get("listOfUsers"));
        if (file.createNewFile())
            this.listOfUsers.toYaml(files.get("listOfUsers"));
        else
            this.listOfUsers.fromYaml(files.get("listOfUsers"));
    }

    public ArrayList<Block> getBlockchain() {
        return this.blockchain;
    }
    public int getNumOfBlocks() {
        return this.numOfBlocks;
    }
    public ArrayList<Transaction> getPool() {
        return this.pool;
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
    public void setNumOfBlocks(int numOfBlocks) {
        this.numOfBlocks = numOfBlocks;
    }
    public void setPool(ArrayList<Transaction> pool) {
        this.pool = pool;
        this.sortPool();
    }
    public void setListOfUsers(ListOfUsers listOfUsers) {
        this.listOfUsers = listOfUsers;
    }
    public void setFiles(LinkedHashMap<String, String> files) {
        this.files = files;
    }

    public boolean checkBlock(Block block) throws NoSuchAlgorithmException {
        Block lastBlock = this.blockchain.get(this.numOfBlocks - 1);
        if (!Objects.equals(block.getPreviousHash(), lastBlock.getHash()))
            return false;
        String hashBlock = Hash.calculateHash(block.toString());
        if (!(hashBlock.startsWith("000000") && Objects.equals(block.getHash(), hashBlock)))
            return false;
        return true;
    }
    public void createTransactionAndAddToPool(String sender, String recipient, double transferSize) {
        if (this.listOfUsers.checkUser(sender) && this.listOfUsers.checkUser(recipient)) {
            if (this.listOfUsers.getUser(sender).getBalance() >= transferSize) {
                Transaction transaction = new Transaction(sender, recipient, transferSize);
                this.pool.add(transaction);
                this.listOfUsers.getUser(sender).decreaseBalance(transferSize);
                this.listOfUsers.getUser(recipient).increaseBalance(transferSize);
                this.sortPool();
            }
        }
    }
    public void addBlock(Block block) throws NoSuchAlgorithmException {
        boolean check;
        if (this.numOfBlocks == 0) {
            check = true;
        }
        else {
            check = checkBlock(block);
        }
        if (check) {
            this.blockchain.add(block);
            this.numOfBlocks++;
            this.pool.clear();
        }
    }
    public Block mineBlock() throws NoSuchAlgorithmException {
        String previousHash;
        if (this.numOfBlocks == 0)
            previousHash = "0";
        else
            previousHash = getBlockchain().get(this.numOfBlocks - 1).getHash();
        if (this.pool.size() != 0) {
            StringBuilder stringOfTransactions = new StringBuilder();
            for (Transaction t : this.pool) {
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
            ArrayList<Transaction> lt = new ArrayList<>();
            for (int i = 0; i < this.pool.size(); i++) {
                Transaction t = new Transaction(this.pool.get(i).getSender(), this.pool.get(i).getRecipient(), this.pool.get(i).getTransferSize());
                lt.add(t);
            }
            return new Block(previousHash, lt, dateOfCreation, proof, hash);
        }
        return null;
    }

    private void sortPool() {
        for (int i = 0; i < this.pool.size(); i++) {
            for (int j = 0; j < this.pool.size(); j++) {
                if (this.pool.get(i).getTransferSize() < this.pool.get(j).getTransferSize()) {
                    double ts = this.pool.get(i).getTransferSize();
                    String s = this.pool.get(i).getSender();
                    String r = this.pool.get(i).getRecipient();

                    this.pool.get(i).setTransferSize(this.pool.get(j).getTransferSize());
                    this.pool.get(j).setTransferSize(ts);

                    this.pool.get(i).setSender(this.pool.get(j).getSender());
                    this.pool.get(j).setSender(s);

                    this.pool.get(i).setRecipient(this.pool.get(j).getRecipient());
                    this.pool.get(j).setRecipient(r);
                }
                else {
                    if (this.pool.get(i).getTransferSize() == this.pool.get(i).getTransferSize()) {
                        if (Integer.parseInt(this.pool.get(i).getSender()) < Integer.parseInt(this.pool.get(j).getSender())) {
                            double ts = this.pool.get(i).getTransferSize();
                            String s = this.pool.get(i).getSender();
                            String r = this.pool.get(i).getRecipient();

                            this.pool.get(i).setTransferSize(this.pool.get(j).getTransferSize());
                            this.pool.get(j).setTransferSize(ts);

                            this.pool.get(i).setSender(this.pool.get(j).getSender());
                            this.pool.get(j).setSender(s);

                            this.pool.get(i).setRecipient(this.pool.get(j).getRecipient());
                            this.pool.get(j).setRecipient(r);
                        }
                        else {
                            if (Integer.parseInt(this.pool.get(i).getSender()) == Integer.parseInt(this.pool.get(j).getSender())) {
                                if (Integer.parseInt(this.pool.get(i).getRecipient()) < Integer.parseInt(this.pool.get(j).getRecipient())) {
                                    double ts = this.pool.get(i).getTransferSize();
                                    String s = this.pool.get(i).getSender();
                                    String r = this.pool.get(i).getRecipient();

                                    this.pool.get(i).setTransferSize(this.pool.get(j).getTransferSize());
                                    this.pool.get(j).setTransferSize(ts);

                                    this.pool.get(i).setSender(this.pool.get(j).getSender());
                                    this.pool.get(j).setSender(s);

                                    this.pool.get(i).setRecipient(this.pool.get(j).getRecipient());
                                    this.pool.get(j).setRecipient(r);
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    public String[] packPool() {
        int numOfTransactions = pool.size();
        String[] transactionsToString = new String[numOfTransactions * 3];
        for (int i = 0; i < numOfTransactions; i++) {
            transactionsToString[i * 3] = pool.get(i).getSender();
            transactionsToString[i * 3 + 1] = pool.get(i).getRecipient();
            transactionsToString[i * 3 + 2] = String.valueOf(pool.get(i).getTransferSize());
        }
        return transactionsToString;
    }

    public ArrayList<Transaction> unpackPool(String[] blockToStrV) {
        int numOfTransactions = (blockToStrV.length - 4) / 3;
        ArrayList<Transaction> listOfTransactions = new ArrayList<>(numOfTransactions);
        for (int i = 0; i < numOfTransactions; i++) {
            listOfTransactions.add(new Transaction(blockToStrV[i * 3 + 1], blockToStrV[i * 3 + 2], Double.parseDouble(blockToStrV[i * 3 + 3])));
        }
        return listOfTransactions;
    }

    public void toYaml(String path) throws FileNotFoundException {
        DumperOptions options = new DumperOptions();
        options.setIndent(2);
        options.setPrettyFlow(true);
        options.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);

        Yaml yamlFile = new Yaml(options);
        LinkedHashMap<String, Object> map = new LinkedHashMap<>();
        ArrayList<LinkedHashMap<String, Object>> mapBlocks = new ArrayList<>();
        ArrayList<LinkedHashMap<String, Object>> mapPool = new ArrayList<>();

        this.blockchain.forEach(block -> mapBlocks.add(block.toLinkedHashMap()));
        this.pool.forEach(transaction -> mapPool.add(transaction.toLinkedHashMap()));

        map.put("blockchain", mapBlocks);
        map.put("numOfBlocks", this.numOfBlocks);
        map.put("pool", mapPool);
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
        this.numOfBlocks = bc.numOfBlocks;
        this.files = bc.files;
    }
}