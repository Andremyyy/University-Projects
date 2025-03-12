module org.example.cumparatori_min_max {
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
    requires org.slf4j;

    opens org.example.cumparatori_min_max to javafx.fxml;
    exports org.example.cumparatori_min_max;
    exports Domain;
    exports Exceptions;
    exports Repository;
    exports Service;
}