package com.example.kevinbolanosbravo.sinterface;

import com.example.kevinbolanosbravo.model.Empleado;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Path;

public interface CrudEmpleadoInterface {

    @GET("/consultarAll")
    Call<List<Empleado>> getAll();

    @POST("/guardar")
    Call<Empleado> createEmployee(@Body Empleado empleado);



    @DELETE("/user/{id}")
    Call<Void> deleteById(@Path("id") int id);


    @GET("/consultar/{id}")
    Call<Empleado> getById(@Path("id") int id);







}
