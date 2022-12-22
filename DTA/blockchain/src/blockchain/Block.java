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

    public String[] pack() {
        int numOfTransactions = listOfTransactions.size();
        String[] transactionsToString = new String[numOfTransactions * 3];
        for (int i = 0; i < numOfTransactions; i++) {
            transactionsToString[i * 3] = listOfTransactions.get(i).getSender();
            transactionsToString[i * 3 + 1] = listOfTransactions.get(i).getRecipient();
            transactionsToString[i * 3 + 2] = String.valueOf(listOfTransactions.get(i).getTransferSize());
        }
        String[] blockToStrV = new String[4 + numOfTransactions * 3];
        blockToStrV[0] = this.previousHash;
        if (numOfTransactions * 3 + 1 - 1 >= 0)
            System.arraycopy(transactionsToString, 0, blockToStrV, 1, numOfTransactions * 3);
        blockToStrV[numOfTransactions * 3 + 1] = String.valueOf(this.dateOfCreation);
        blockToStrV[numOfTransactions * 3 + 2] = String.valueOf(this.proof);
        blockToStrV[numOfTransactions * 3 + 3] = this.hash;
        return blockToStrV;
    }

    public Block unpack(String[] blockToStrV) {
        String previousHash = blockToStrV[0];
        int numOfTransactions = (blockToStrV.length - 4) / 3;
        ArrayList<Transaction> listOfTransactions = new ArrayList<>(numOfTransactions);
        for (int i = 0; i < numOfTransactions; i++) {
            listOfTransactions.add(new Transaction(blockToStrV[i * 3 + 1], blockToStrV[i * 3 + 2], Double.parseDouble(blockToStrV[i * 3 + 3])));
        }
        long dateOfCreation = Long.parseLong(blockToStrV[numOfTransactions * 3 + 1]);
        int proof = Integer.parseInt(blockToStrV[numOfTransactions * 3 + 2]);
        String hash = blockToStrV[numOfTransactions * 3 + 3];
        return new Block(previousHash, listOfTransactions, dateOfCreation, proof, hash);
    }

    @Override
    public String toString() {
        StringBuilder listOfTransactions = new StringBuilder();
        for (Transaction t : this.listOfTransactions) {
            listOfTransactions.append(t.toString());
        }
        return this.previousHash + listOfTransactions + this.dateOfCreation + this.proof;
    }
}