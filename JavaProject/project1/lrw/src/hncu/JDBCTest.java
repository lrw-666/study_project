package hncu;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class JDBCTest {
    public static void main(String[] args) throws Exception{
        // 标准格式
        Class.forName("com.mysql.jdbc.Driver");
        Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "root");
        String sql = "";
        PreparedStatement prepareStatement = connection.prepareStatement(sql);
        ResultSet resultSet = prepareStatement.executeQuery();
        while(resultSet.next()){
            System.out.println("hhh");
        }
        connection.close();
        prepareStatement.close();
        resultSet.close();

        // 创建数据库:CREATE DATABASE mybase;
        // 删除数据库:drop database 数据库名称;
        // 查看数据库：show databases;
        // 删除数据库:drop database;
        // 使用数据库:USE mybase;

        // 创建数据表：create table 表名(
        //          列名1 数据类型 约束,
        //          列名2 数据类型 约束,
        //          列名3 数据类型 约束
        //      );
//        将编号列,设置为主键约束,保证列的数据唯一性,非空性 primary key AUTO_INCREMENT

//        向数据表中添加数据 insert
//        格式:insert into 表名(列名1,列名2,列名3) values (值1,值2,值3),(值1,值2,值3)

        // 数据在原有的基础上修改
        //   格式: update 表名 set 列1=值1,列2=值2 where 条件

        // 删除表中的数据
        //  格式: delete from 表名 where 条件

        // 查询所有列的数据
        //  格式: select * from 表名
    }
}
