module org.example.radio_fire_de_executie {
    requires javafx.controls;
    requires javafx.fxml;
    requires javafx.web;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires net.synedra.validatorfx;
    requires org.kordamp.ikonli.javafx;
    requires org.kordamp.bootstrapfx.core;
    requires eu.hansolo.tilesfx;
    requires com.almasb.fxgl.all;
    requires java.sql;
    requires org.xerial.sqlitejdbc;

    opens org.example.radio_fire_de_executie to javafx.fxml;
    exports org.example.radio_fire_de_executie;
    exports Domain;
    exports Repository;
    exports Service;
    exports Exceptions;
}