package blockchain;

import java.util.LinkedHashMap;

public class User {
    private String walletId;
    private double balance;

    public User() {}

    public User(String walletId, double balance) {
        this.walletId = walletId;
        this.balance = balance;
    }

    public String getWalletId() {
        return this.walletId;
    }
    public double getBalance() {
        return this.balance;
    }

    public void setWalletId(String walletId) {
        this.walletId = walletId;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public LinkedHashMap<String, Object> toLinkedHashMap() {
        LinkedHashMap<String, Object> map = new LinkedHashMap<>();
        map.put("walletId", this.walletId);
        map.put("balance", this.balance);
        return map;
    }

    @Override
    public boolean equals(Object object) {
        boolean result = false;
        if (object != null && object instanceof User) {
            User user = (User)object;
            if (user.getWalletId() == this.getWalletId() && user.getBalance() == this.getBalance())
                result = true;
        }
        return result;
    }
}
