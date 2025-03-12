module org.example.cumparaturi {
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

    opens org.example.cumparaturi to javafx.fxml;
    exports org.example.cumparaturi;
    exports Domain;
    exports Exceptions;
    exports Repository;
    exports Service;
}