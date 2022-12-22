package blockchain;

import java.util.ArrayList;
import java.util.LinkedHashMap;

public class Transaction {
    private String sender;
    private String recipient;
    private double transferSize;

    public Transaction() {}

    public Transaction(String sender, String recipient, double transferSize) {
        this.sender = sender;
        this.recipient = recipient;
        this.transferSize = transferSize;
    }

    public String getSender() {
        return this.sender;
    }
    public String getRecipient() {
        return this.recipient;
    }
    public double getTransferSize() {
        return this.transferSize;
    }

    public void setSender(String sender) {
        this.sender = sender;
    }

    public void setRecipient(String recipient) {
        this.recipient = recipient;
    }

    public void setTransferSize(double transferSize) {
        this.transferSize = transferSize;
    }

    public LinkedHashMap<String, Object> toLinkedHashMap() {
        LinkedHashMap<String, Object> map = new LinkedHashMap<>();
        map.put("sender", this.sender);
        map.put("recipient", this.recipient);
        map.put("transferSize", this.transferSize);
        return map;
    }

    @Override
    public String toString() {
        return this.sender + this.recipient + this.transferSize;
    }
}
