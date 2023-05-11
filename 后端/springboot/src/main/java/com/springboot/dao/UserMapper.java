package com.springboot.dao;

import com.springboot.pojo.User;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Service;

import java.util.List;

@Mapper
public interface UserMapper {
    public List<User> findAll();
    public User login(String phone,String password);
    public User findByPhone(String phone);

    public User findById(String id,String seatNum);
    public void register(String phone,String password);
    public int changeOpen(boolean flag,String phone);
    public int update(User user);
}
