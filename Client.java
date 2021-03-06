package com.test.client;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class Client {

    public static void main(String[] args) {
        new Client().startClient();
    }

    public void startClient(){
        try {
            //连接到服务器
            Socket socket = new Socket("localhost", 9999);
            DataInputStream dis = new DataInputStream(socket.getInputStream());
            DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
            Scanner scanner = new Scanner(System.in);
            String line = null;
            listenServerReply(dis);
            while((line = scanner.nextLine()) != null){//读取从键盘输入的一行
                dos.writeUTF(line);//发给服务端
                System.out.println("client send msg : " + line);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    //监听服务端回复的消息
    public void listenServerReply(final DataInputStream dis){
        new Thread(){
            @Override
            public void run() {
                super.run();
                String line = null;
                try {
                    while((line = dis.readUTF()) != null){
                        System.out.println("client receive msg from server: " + line);
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }.start();
    }

}