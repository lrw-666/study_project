package hncu;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;

public class GUITest {
    public static void main(String[] args) {
        // 鼠标点击位置显示
//        JFrame frame = new JFrame();
//        frame.setSize(300, 400);
//        frame.setResizable(false);
//        frame.setLocationRelativeTo(null);
//        final JLabel label = new JLabel("此处显示鼠标右键单击的坐标");
//        frame.add(label, BorderLayout.NORTH);
//        frame.setVisible(true);
//
//        frame.addMouseListener(new MouseAdapter() {
//            @Override
//            public void mouseClicked(MouseEvent e) {
//                super.mouseClicked(e);
//                if(e.getButton()==MouseEvent.BUTTON1){
//                    label.setText("当前鼠标点击位置是：" + e.getX() + ":" + e.getY());
//                }
//            }
//        });

        // 多重面板
        JFrame frame = new JFrame();
        frame.setSize(800, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        // 设置组件
        JPanel panel = new JPanel();
        panel.setSize(600, 200);
        panel.setLayout(new FlowLayout());
        JLabel label = new JLabel("兴趣");
        JLabel label1 = new JLabel("性别");
        JCheckBox box = new JCheckBox("羽毛球");
        JCheckBox box1 = new JCheckBox("乒乓球");
        JCheckBox box2 = new JCheckBox("唱歌");
        final JRadioButton button = new JRadioButton("男");
        final JRadioButton button1 = new JRadioButton("女");
        ButtonGroup group = new ButtonGroup();
        group.add(button);
        group.add(button1);
        button.setSelected(true);
        panel.add(label);
        panel.add(box);
        panel.add(box1);
        panel.add(box2);
        panel.add(label1);
        panel.add(button);
        panel.add(button1);
        frame.add(panel, BorderLayout.NORTH);

        final JTextArea area = new JTextArea();
        area.setEditable(false);
        JScrollPane pane = new JScrollPane(area);
        frame.add(pane, BorderLayout.CENTER);
        frame.setVisible(true);
        // 创建兴趣列表
        final ArrayList<String> interest = new ArrayList<>();
        // 设置复选框监听事件
        ActionListener listener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JCheckBox source = (JCheckBox) e.getSource();// 最初发生 Event 的对象。
                area.setText("");
                if(source.isSelected()){
                    interest.add(source.getText());
                }else {
                    interest.remove(source.getText());
                }
                if(interest.size() > 0){
                    area.setText("你的兴趣爱好有：");
                    for(String str:interest){
                        area.append(" " + str);
                    }
                }
                area.append("\n你的性别为:");
                if(button.isSelected()){
                    area.append(button.getText());
                }else{
                    area.append(button1.getText());
                }
            }
        };
        box.addActionListener(listener);
        box1.addActionListener(listener);
        box2.addActionListener(listener);

        // 设置单选框监听
        ActionListener listener1 = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                area.setText("");
                if(interest.size() > 0){
                    area.setText("你的兴趣爱好有：");
                    for(String str:interest){
                        area.append(" " + str);
                    }
                }
                area.append("\n你的性别为:");
                if(button.isSelected()){
                    area.append(button.getText());
                }else{
                    area.append(button1.getText());
                }
            }
        };
        button.addActionListener(listener1);
        button1.addActionListener(listener1);
    }
}
