package com.example.kevinbolanosbravo;
//KEVIN ALEXANDER BOLAÑOS BRAVO
import android.os.Bundle;
import android.util.Log;

import androidx.appcompat.app.AppCompatActivity;

import com.example.kevinbolanosbravo.model.Empleado;
import com.example.kevinbolanosbravo.sinterface.CrudEmpleadoInterface;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


public class MainActivity extends AppCompatActivity {

    private CrudEmpleadoInterface cruempleado;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //ConsultaTodo
        getAll();

        //guardar empleado
        saveUser("kevin.bolanos00@ejemplo.com", "Kevin Bolanos", "123");

        //Consultar por id
        getById(2);

        //Eliminar por Id
        deleteById(3);

    }

    private void getAll(){
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://192.168.1.7:8081")
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        cruempleado = retrofit.create(CrudEmpleadoInterface.class);
        Call<List<Empleado>> call= cruempleado.getAll();

        call.enqueue(new Callback<List<Empleado>>(){
            @Override
            public void onResponse(Call<List<Empleado>> call, Response<List<Empleado>> response) {
                if (!response.isSuccessful()){
                    //System.out.println(response.message());
                    Log.e("Response err:", response.message());
                    return;
                }
                List<Empleado> listempleado;
                listempleado= response.body();

                listempleado.forEach(p-> System.out.println(p.toString()));
            }
            @Override
            public void onFailure(Call<List<Empleado>> call, Throwable t){
                Log.e("Throw error", t.getMessage());
            }


        });
    }

    private void saveUser(String email, String nombre, String password) {
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://192.168.1.7:8081")
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        CrudEmpleadoInterface crudEmpleado = retrofit.create(CrudEmpleadoInterface.class);

        Empleado newEmpleado = new Empleado(email, nombre, password);

        Call<Empleado> call = crudEmpleado.createEmployee(newEmpleado);

        call.enqueue(new Callback<Empleado>() {
            @Override
            public void onResponse(Call<Empleado> call, Response<Empleado> response) {
                if (!response.isSuccessful()) {
                    Log.e("Response error:", response.message());
                    return;
                }
                Empleado empleadoResponse = response.body();
                Log.i("Empleado guardado:", empleadoResponse.toString());
            }

            @Override
            public void onFailure(Call<Empleado> call, Throwable t) {
                Log.e("Throw error", t.getMessage());
            }
        });
    }

    private void getById(int id){
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://192.168.1.7:8081")
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        CrudEmpleadoInterface crudEmpleado = retrofit.create(CrudEmpleadoInterface.class);
        Call<Empleado> call = crudEmpleado.getById(id);

        call.enqueue(new Callback<Empleado>() {
            @Override
            public void onResponse(Call<Empleado> call, Response<Empleado> response) {
                if (!response.isSuccessful()) {
                    Log.e("Response err: ocurrio un error", response.message());
                    return;
                }
                Empleado empleado = response.body();
                System.out.println(empleado.toString());
            }

            @Override
            public void onFailure(Call<Empleado> call, Throwable t) {
                Log.e("Throw error", t.getMessage());
            }
        });
    }


    private void deleteById(int id) {
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://192.168.1.7:8081")
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        CrudEmpleadoInterface crudEmpleado = retrofit.create(CrudEmpleadoInterface.class);
        Call<Void> call = crudEmpleado.deleteById(id);

        call.enqueue(new Callback<Void>() {
            @Override
            public void onResponse(Call<Void> call, Response<Void> response) {
                if (!response.isSuccessful()) {
                    Log.e("Response err:", response.message());
                    return;
                }
                Log.d("Delete success:", "User deleted successfully");
            }

            @Override
            public void onFailure(Call<Void> call, Throwable t) {
                Log.e("Throw error", t.getMessage());
            }
        });
    }




}
