package blockchain;
import mpi.*;

import java.io.*;
import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.Date;
import java.util.LinkedHashMap;

public class Main {
    public static void main(String[] args)
            throws Exception {
        MPI.Init(args);
        int rank = MPI.COMM_WORLD.Rank();
        int size = MPI.COMM_WORLD.Size();

        if (rank == 0) {
            LinkedHashMap<String, String> files = new LinkedHashMap<>();
            files.put("blockchain", "src/blockchain/blockchain2.yaml");
            files.put("listOfUsers", "src/blockchain/listOfUsers2.yaml");

            Blockchain b = new Blockchain(files);
            ArrayList<Transaction> t = new ArrayList<>();
            Transaction t1 = new Transaction(b.getListOfUsers().listOfUsers.get(1).getWalletId(), b.getListOfUsers().listOfUsers.get(2).getWalletId(), 100.01);
            Transaction t2 = new Transaction(b.getListOfUsers().listOfUsers.get(2).getWalletId(), b.getListOfUsers().listOfUsers.get(0).getWalletId(), 500);
            t.add(t1);
            t.add(t2);
            b.mineAndAddBlock(t);
            b.toYaml("src/blockchain/blockchain2_out.yaml");
        }

//        String[] transaction = new String[3];
//        transaction[0] = "00000001";
//        transaction[1] = "00000005";
//        transaction[2] = "10.2";

//        if (rank == 0) {
//            MPI.COMM_WORLD.Send(transaction, 0, transaction.length, MPI.OBJECT, 1, 0);
//        }
//        else
//            if (rank == 1) {
//                MPI.COMM_WORLD.Recv(transaction, 0, transaction.length, MPI.OBJECT, 0, 0);
//            }

//        if (rank <= 1) {
//            ArrayList<Transaction> listTransactions = new ArrayList<>();
//            Transaction t1 = new Transaction("00000001", "00000005", 10.2);
//            Transaction t2 = new Transaction("00000002", "00000003", 9.87);
//            listTransactions.add(t1);
//            listTransactions.add(t2);
//
//            String[] transaction = new String[6];
//            transaction[0] = listTransactions.get(0).getSender();
//            transaction[1] = listTransactions.get(0).getRecipient();
//            transaction[2] = String.valueOf(listTransactions.get(0).getTransferSize());
//            transaction[3] = listTransactions.get(1).getSender();
//            transaction[4] = listTransactions.get(1).getRecipient();
//            transaction[5] = String.valueOf(listTransactions.get(1).getTransferSize());
//
//            String[] block = new String[10];
//            block[0] = "0";
//            System.arraycopy(transaction, 0, block, 1, transaction.length);
//            block[transaction.length + 1] = String.valueOf(new Date().getTime());
//            block[transaction.length + 2] = String.valueOf(396036566);
//            block[transaction.length + 3] = "5ad3c61812efbc0a71dd50dd6464d9186894888818c1a6acb20bf0d5ae1e366a";
//            MPI.COMM_WORLD.Send(new int[]{block.length}, 0, 1, MPI.INT, 1, 0);
//            MPI.COMM_WORLD.Send(block, 0, block.length, MPI.OBJECT, 2, 0);
//
////            Block b1 = new Block("0", listTransactions, new Date().getTime(), 396036566, "5ad3c61812efbc0a71dd50dd6464d9186894888818c1a6acb20bf0d5ae1e366a");
//
//        }
//        else
//        if (rank == 2) {
//            int[] len = new int[1];
//            MPI.COMM_WORLD.Recv(len, 0, 1, MPI.INT, MPI.ANY_SOURCE, 0);
//            String[] b = new String[len[0]];
//            MPI.COMM_WORLD.Recv(b, 0, b.length, MPI.OBJECT, MPI.ANY_SOURCE, 0);
//            StringBuilder s = new StringBuilder();
//            for (String i : b)
//                s.append(i).append("  ");
//            System.out.println(s);
//        }
        MPI.Finalize();
    }
}
