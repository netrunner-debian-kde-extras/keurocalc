project( keurocalc )

########### next target ###############

set( keurocalc_SRCS
   ../currencies/currencies.cpp
   keurocalc.cpp
   main.cpp
   preferences.cpp )

qt4_add_resources(keurocalc_SRCS keurocalc.qrc)

kde4_add_ui_files( keurocalc_SRCS
   calculator.ui
   settingsdialog.ui )

kde4_add_executable(keurocalc ${keurocalc_SRCS} )

target_link_libraries(keurocalc ${KDE4_KIO_LIBS} ${KDE4_KDEUI_LIBS} )

install(TARGETS keurocalc ${INSTALL_TARGETS_DEFAULT_ARGS} )


########### install files ###############

install( PROGRAMS keurocalc.desktop DESTINATION ${XDG_APPS_INSTALL_DIR} )

install( FILES splash.png ../currencies/currencies.xml DESTINATION ${DATA_INSTALL_DIR}/keurocalc )

kde4_install_icons( ${ICON_INSTALL_DIR} )
