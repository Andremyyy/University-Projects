module org.example.a4javafx {
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
    requires com.fasterxml.jackson.annotation;
    requires com.fasterxml.jackson.databind;
    requires javafaker;
    requires org.xerial.sqlitejdbc;

    opens org.example.a4javafx to javafx.fxml;
    opens Domain;
    opens Exceptions;
    exports Repository;
    exports Exceptions;
    exports Domain;
    exports org.example.a4javafx;
}