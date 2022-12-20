package blockchain;

import java.util.ArrayList;
import java.util.LinkedHashMap;

public class Block {
    private String hash;
    private String previousHash;
    private ArrayList<Transaction> listOfTransactions;
    private long dateOfCreation;
    private int proof;

    public Block() {}

    public Block(String previousHash, ArrayList<Transaction> listOfTransactions, long dateOfCreation, int proof, String hash) {
        this.previousHash = previousHash;
        this.listOfTransactions = listOfTransactions;
        this.dateOfCreation = dateOfCreation;
        this.proof = proof;
        this.hash = hash;
    }

    public String getHash() {
        return this.hash;
    }

    public String getPreviousHash() {
        return this.previousHash;
    }

    public ArrayList<Transaction> getListOfTransactions() {
        return this.listOfTransactions;
    }

    public long getDateOfCreation() {
        return this.dateOfCreation;
    }

    public int getProof() {
        return this.proof;
    }

    public void setHash(String hash) {
        this.hash = hash;
    }

    public void setPreviousHash(String previousHash) {
        this.previousHash = previousHash;
    }

    public void setListOfTransactions(ArrayList<Transaction> listOfTransactions) {
        this.listOfTransactions = listOfTransactions;
    }

    public void setDateOfCreation(long dateOfCreation) {
        this.dateOfCreation = dateOfCreation;
    }

    public void setProof(int proof) {
        this.proof = proof;
    }

    public LinkedHashMap<String, Object> toLinkedHashMap() {
        LinkedHashMap<String, Object> map = new LinkedHashMap<>();
        ArrayList<LinkedHashMap<String, Object>> mapTransactions = new ArrayList<>();
        this.listOfTransactions.forEach(transaction -> mapTransactions.add(transaction.toLinkedHashMap()));

        map.put("hash", this.hash);
        map.put("previousHash", this.previousHash);
        map.put("listOfTransactions", mapTransactions);
        map.put("dateOfCreation", this.dateOfCreation);
        map.put("proof", this.proof);
        return map;
    }

//    @Override
//    public String toString() {
//        StringBuilder listOfTransactions = new StringBuilder();
//        for (Transaction t : this.listOfTransactions) {
//            listOfTransactions.append(t.toString());
//        }
//        return this.hash + this.previousHash + listOfTransactions + this.dateOfCreation + this.proof;
//    }
}