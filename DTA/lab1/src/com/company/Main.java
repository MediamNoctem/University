package com.company;
import mpi.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.io.*;


public class Main {
    public static void ex1(int[] message, int rank, int size) {
        if (rank % 2 == 0) {
            if (rank < size - 1) {
                MPI.COMM_WORLD.Send(message, 0, 1, MPI.INT, rank + 1, 0);
                System.out.println("send: from rank " + rank + " " + Arrays.toString(message));
            }
        } else {
            MPI.COMM_WORLD.Recv(message, 0, 1, MPI.INT, rank - 1, 0);
            System.out.println("received: from rank " + (rank - 1) + " " + Arrays.toString(message));
        }
    }

    public static void ex2(int[] s, int rank, int size) {
        if (rank == 0) {
            MPI.COMM_WORLD.Send(s, 0, 1, MPI.INT, rank + 1, 0);
            System.out.println("send: from rank " + rank + " " + Arrays.toString(s));

            MPI.COMM_WORLD.Recv(s,0, 1, MPI.INT, size - 1, 0);
            System.out.println("received: from rank " + rank + " " + Arrays.toString(s));
        }
        else {
            MPI.COMM_WORLD.Recv(s,0, 1, MPI.INT, rank - 1, 0);
            System.out.println("received: from rank " + rank + " " + Arrays.toString(s));

            MPI.COMM_WORLD.Send(s, 0, 1, MPI.INT, (rank + 1) % size, 0);
            System.out.println("send: from rank " + rank + " " + Arrays.toString(s));
        }
    }

    public static boolean check_array(int[] array) {
        for (int i = 0; i < array.length - 2; i++)
            if (array[i] > array[i + 1]) return true;
        return false;
    }

    public static void sort_(int[] array, int size, int rank) {
        boolean flag = true;
        int n = array.length;
        if (n > 1) {
            int beginning_selection_pairs = 1;
            int array_div_2 = n / 2;
            int number_pairs;
            int number_active_processors;
            int max_number_active_processors;
            int[] number_iterations_per_processor;
            Request[] req, req1;
            Request r;

            while (flag) {
                beginning_selection_pairs = 1 - beginning_selection_pairs;
                number_pairs = n % 2 == 0 ? array_div_2 - beginning_selection_pairs : array_div_2;
                number_active_processors = Math.min(size, number_pairs);
                max_number_active_processors = Math.min(size, array_div_2);
                number_iterations_per_processor = new int[number_active_processors];
                for (int i = 0; i < number_active_processors; i++)
                    number_iterations_per_processor[i] = (i < number_pairs % number_active_processors) ? (number_pairs / number_active_processors + 1) : (number_pairs / number_active_processors);
                req = new Request[number_pairs + 1];
                req1 = new Request[max_number_active_processors];

//                System.out.println("-----------------------------------------------------");
//                System.out.println("flag = " + flag);
//                System.out.println("beginning_selection_pairs = " + beginning_selection_pairs);
//                System.out.println("number_pairs = " + number_pairs);
//                System.out.println("number_active_processors = " + number_active_processors);
//                System.out.println("max_number_active_processors = " + max_number_active_processors);
//                System.out.println("number_iterations_per_processor = " + Arrays.toString(number_iterations_per_processor));

                if (rank < max_number_active_processors) {
                    if (rank == 0) {
                        for (int j = 1; j < number_active_processors; j++)
                            for (int i = 0; i < number_iterations_per_processor[j]; i++)
                                req[j - 1 + i * number_active_processors] = MPI.COMM_WORLD.Irecv(array, j * 2 + i * number_active_processors * 2 + beginning_selection_pairs, 2, MPI.INT, j, 0);

                        Request.Waitall(req);

                        for (int i = 0; i < number_iterations_per_processor[0]; i++) {
                            if (array[i * number_active_processors * 2 + beginning_selection_pairs] > array[i * number_active_processors * 2 + 1 + beginning_selection_pairs]) {
                                int tmp = array[i * number_active_processors * 2 + beginning_selection_pairs];
                                array[i * number_active_processors * 2 + beginning_selection_pairs] = array[i * number_active_processors * 2 + 1 + beginning_selection_pairs];
                                array[i * number_active_processors * 2 + 1 + beginning_selection_pairs] = tmp;
                            }
                        }
                        for (int j = 1; j < max_number_active_processors; j++)
                            req1[j - 1] = MPI.COMM_WORLD.Isend(array, 0, n, MPI.INT, j, 0);

                        Request.Waitall(req1);
                    } else {
                        if (rank < number_active_processors) {
                            for (int i = 0; i < number_iterations_per_processor[rank]; i++) {
                                if (array[rank * 2 + i * number_active_processors * 2 + beginning_selection_pairs] > array[rank * 2 + i * number_active_processors * 2 + 1 + beginning_selection_pairs]) {
                                    int tmp = array[rank * 2 + i * number_active_processors * 2 + beginning_selection_pairs];
                                    array[rank * 2 + i * number_active_processors * 2 + beginning_selection_pairs] = array[rank * 2 + i * number_active_processors * 2 + 1 + beginning_selection_pairs];
                                    array[rank * 2 + i * number_active_processors * 2 + 1 + beginning_selection_pairs] = tmp;
                                }
                                r = MPI.COMM_WORLD.Isend(array, rank * 2 + i * number_active_processors * 2 + beginning_selection_pairs, 2, MPI.INT, 0, 0);
                                r.Wait();
                            }
                        }
                        r = MPI.COMM_WORLD.Irecv(array, 0, n, MPI.INT, 0, 0);
                        r.Wait();
                    }

                    flag = check_array(array);

                    System.out.println("Processor " + rank + ": " + Arrays.toString(array));
                }
                else break;
            }
//            System.out.println("Processor " + rank + ", flag = " + flag);
        }
    }

    public static ArrayList<int[]> readMatrixFromFile(String path) {
        ArrayList<int[]> adjacencyMatrix = new ArrayList<>();
        try {
            try (BufferedReader in = new BufferedReader(new FileReader(path))) {
                String str;
                while ((str = in.readLine()) != null) {
                    int len = str.length() / 2 + 1;
                    int[] c = new int[len];
                    for (int i = 0; i < len; i++)
                        c[i] = str.toCharArray()[i * 2] - 48;
                    adjacencyMatrix.add(c);
                }
            }
        } catch (IOException e) {
            System.out.println("Error!");
        }
        return adjacencyMatrix;
    }

    public static ArrayList<int[]> complementMatrixWithZeros(ArrayList<int[]> m, int number_active_processors) {
        int dimension_of_matrix = m.size();
        int number_iterations_per_processor0 = (0 < dimension_of_matrix % number_active_processors) ? (dimension_of_matrix / number_active_processors + 1) : (dimension_of_matrix / number_active_processors);
        int new_size = number_iterations_per_processor0 * number_active_processors;

        ArrayList<int[]> new_m = new ArrayList<>();
        for (int i = 0; i < new_size; i++) {
            int[] tmp = new int[new_size];
            if (i < dimension_of_matrix)
                System.arraycopy(m.get(i), 0, tmp, 0, dimension_of_matrix);
            new_m.add(tmp);
        }
        return new_m;
    }

    public static int maximumDegreeOfGraphVertex(ArrayList<int[]> adjacencyMatrix, int size, int rank) {
        int dimension_of_matrix = adjacencyMatrix.size();
        int number_active_processors = Math.min(size, dimension_of_matrix);
        adjacencyMatrix = complementMatrixWithZeros(adjacencyMatrix, number_active_processors);
        dimension_of_matrix = adjacencyMatrix.size();
        int index = rank;
        int[] tmp_maximum_degree = new int[] {0};
        int[] maximum_degree = new int[] {0, 0};

        if (rank < number_active_processors) {
            while (index < dimension_of_matrix) {
                for (int i = 0; i < dimension_of_matrix; i++) {
                    tmp_maximum_degree[0] += adjacencyMatrix.get(index)[i] | adjacencyMatrix.get(i)[index];
                }
                MPI.COMM_WORLD.Reduce(tmp_maximum_degree, 0, maximum_degree, 0, 1, MPI.INT, MPI.MAX, 0);
                index += number_active_processors;
                maximum_degree[1] = Math.max(maximum_degree[0], maximum_degree[1]);
                tmp_maximum_degree[0] = 0;
            }
        }
        return maximum_degree[1];
    }

    public static boolean isGraphHypercubeParallel(int rank, int size, int n, int[] arr, int razm) {
        MPI.COMM_WORLD.Bcast(arr, 0, n * n, MPI.INT, 0);

        int[] temp_sum = new int[3];
        for (int i = 0; i < n / size + (n % size > 0 ? 1 : 0); i++) {
            temp_sum[1] = 0;
            if (rank + size * i < n) {
                for (int j = n * (rank + size * i) + rank + size * i; j < n * (rank + size * i + 1); j++) {
                    temp_sum[0] += arr[j];
                }
                for (int j = n * (rank + size * i); j < n * (rank + size * i + 1); j++) {
                    temp_sum[1] += arr[j];
                }
                if(temp_sum[1] != razm) temp_sum[2] += 1;
            }
        }
        int[] sum = new int[2];
        int[] t_sum = new int[2];
        t_sum[0] = temp_sum[0];
        t_sum[1] = temp_sum[2];

        MPI.COMM_WORLD.Reduce(t_sum, 0, sum, 0, 2, MPI.INT, MPI.SUM, 0);
        if (rank == 0) return sum[1] == 0 && ((n & (n - 1)) == 0) && sum[0] == (Math. pow(2,(razm-1)) * razm);
        return false;
    }

    public static boolean isGraphHypercubeSerial(int n, int[] arr, int razm) {
        int sum = 0;
        for(int i = 0; i < n; i++)
            for(int j = i; j<n; j++) {
                sum += arr[i*n+j];
            }
        int sum2 = 0,sum3=0;
        for(int i = 0; i < n; i++){
            sum2=0;
            for(int j = 0; j<n; j++)
                sum2 += arr[i*n+j];
            if(sum2!=razm) sum3++;
        }
        return sum3 == 0 && ((n & (n - 1)) == 0) && sum == (Math. pow(2,(razm-1)) * razm);
    }

    public static void main(String[] args)
            throws Exception {
        /*int[] s = { 0 };
        int[] data = { 2016 };
        int[] buf = { 1, 3, 5 };
        int count, TAG = 0;
        Status st;
        int[] mas = { 14, 5, 9, 0, 80, 3, 1, 15 };
        */
        MPI.Init(args);
        int rank = MPI.COMM_WORLD.Rank();
        int size = MPI.COMM_WORLD.Size();

        if (size == 1) {
            System.out.println("Error!");
            MPI.Finalize();
            return;
        }
//        #1
        /*int[] message = { rank };
        ex1(message, rank, size);*/

//        #2
        /*ex2(s,rank, size);
        */

//        #3
        /*sort_(mas, size,rank);
        if (rank == 0)
            System.out.println("Result: " + Arrays.toString(mas));*/

//        #4
        /*if (rank == 0) {
            MPI.COMM_WORLD.Send(data, 0, 1, MPI.INT, 2, TAG);
            System.out.print("send: Rank = " + rank + "\n");
        } else if (rank == 1) {
            MPI.COMM_WORLD.Send(buf, 0, buf.length, MPI.INT, 2, TAG);
            System.out.print("send: Rank = " + rank + "\n");
        } else if (rank == 2) {
            st = MPI.COMM_WORLD.Probe(0, TAG);
            count = st.Get_count(MPI.INT);
            MPI.COMM_WORLD.Recv(buf, 0, count, MPI.INT, 0, TAG);
            System.out.print("Rank = 0\n");
            for (int i = 0; i < count; i++)
                System.out.print(buf[i] + " ");
            System.out.print("\n");
            st = MPI.COMM_WORLD.Probe(1, TAG);
            count = st.Get_count(MPI.INT);
            MPI.COMM_WORLD.Recv(buf, 0, count, MPI.INT, 1, TAG);
            System.out.print("Rank = 1\n");
            for (int i = 0; i < count; i++)
                System.out.print(buf[i] + " ");
            System.out.print("\n");
        }*/

//        #7-8
//        №1
        ArrayList<int[]> adjacencyMatrix = readMatrixFromFile("src/com/company/graph2.txt");
        int m = maximumDegreeOfGraphVertex(adjacencyMatrix,size,rank);
        if (rank == 0) {
            for (int i = 0; i < adjacencyMatrix.size(); i++) {
                System.out.println(Arrays.toString(adjacencyMatrix.get(i)));
            }
            System.out.println("Maximum degree of graph vertex = " + m);
        }
//        №2
        /*ArrayList<int[]> adjacencyMatrix = readMatrixFromFile("src/com/company/graph4.txt");

        int[] N = {1000, 2500, 4000};
        for (int n : N) {
            int[] arr = new int[n * n];
            long time = 0;
            if (rank == 0) {
                System.out.println("n = " + n);

            arr = new int[]{0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0};
//            arr = new int[]{
//                    0,1,0,1,0,0,1,0,
//                    1,0,1,0,0,0,0,1,
//                    0,1,0,1,1,0,0,0,
//                    1,0,1,0,0,1,0,0,
//                    0,0,1,0,0,1,0,1,
//                    0,0,0,1,1,0,1,0,
//                    1,0,0,0,0,1,0,1,
//                    0,1,0,0,1,0,1,0
//            };
//                arr = gen_matr_gipercube(n,4);

                time = System.currentTimeMillis();
            }
            for(int i = 1; i<5;i++) {
                boolean res = false;
//      res = lab8(rank, size, n, arr, i);
                if (rank == 0) res = lab8_posled_alg(n,arr,i);
                if(rank == 0)
                    System.out.println("for dimension = " + i + " -> " + res);
                if(res) break;
            }
            if (rank == 0) {
                long t = System.currentTimeMillis();
                System.out.println("Time = " + (t - time) + " ms");
            }
        }*/

        MPI.Finalize();
    }
}