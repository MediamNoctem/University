package blockchain;

import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import java.io.*;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Objects;

public class ListOfUsers {
    private ArrayList<User> listOfUsers;

    public ListOfUsers() {
        this.listOfUsers = new ArrayList<>();
    }

    public ArrayList<User> getListOfUsers() {
        return this.listOfUsers;
    }

    public void setListOfUsers(ArrayList<User> listOfUsers) {
        this.listOfUsers = listOfUsers;
    }

    public User getUser(String walletId) {
        for (User user : this.listOfUsers)
            if (Objects.equals(user.getWalletId(), walletId))
                return user;
        return null;
    }

    public void addUser(String walletId, double balance) {
        if (!checkUser(walletId)) {
            User user = new User(walletId, balance);
            this.listOfUsers.add(user);
        }
    }

    public boolean checkUser(String walletId) {
        for (User userFromList : this.listOfUsers)
            if (Objects.equals(userFromList.getWalletId(), walletId))
                return true;
        return false;
    }

    public void toYaml(String path) throws FileNotFoundException {
        DumperOptions options = new DumperOptions();
        options.setIndent(2);
        options.setPrettyFlow(true);
        options.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);

        Yaml yamlFile = new Yaml(options);
        LinkedHashMap<String, Object> map = new LinkedHashMap<>();
        ArrayList<LinkedHashMap<String, Object>> mapUsers = new ArrayList<>();

        this.listOfUsers.forEach(user -> mapUsers.add(user.toLinkedHashMap()));
        map.put("listOfUsers", mapUsers);

        PrintWriter doc = new PrintWriter(path);
        yamlFile.dump(map, doc);
    }

    public void fromYaml(String path) {
        this.listOfUsers.clear();
        Yaml yaml = new Yaml(new Constructor(ListOfUsers.class));
        InputStream inputStream = ListOfUsers.class
                .getClassLoader()
                .getResourceAsStream(path);
        this.listOfUsers = ((ListOfUsers)yaml.load(inputStream)).listOfUsers;
    }
}
