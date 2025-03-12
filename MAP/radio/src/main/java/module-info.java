module org.example.radio {
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
    requires java.sql;
    requires org.xerial.sqlitejdbc;

    opens org.example.radio to javafx.fxml;
    opens Repository;
    opens Service;
    opens Domain;
    opens Exceptions;
    exports Repository;
    exports Service;
    exports Domain;
    exports Exceptions;
    exports org.example.radio;
}