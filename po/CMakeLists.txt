project(po)

FILE(GLOB _pofiles *.po)
FOREACH(_infile ${_pofiles})
    GET_FILENAME_COMPONENT(_lang ${_infile} NAME_WE)
    GET_FILENAME_COMPONENT(_outfile ${CMAKE_CURRENT_BINARY_DIR}/${_lang}.mo ABSOLUTE)

    ADD_CUSTOM_COMMAND(
        OUTPUT ${_outfile}
        COMMAND msgfmt -o ${_outfile} ${_infile}
        DEPENDS ${_infile})

    INSTALL(
        FILES ${_outfile}
        DESTINATION ${LOCALE_INSTALL_DIR}/${_lang}/LC_MESSAGES/
        RENAME keurocalc.mo)

    SET(_sources ${_sources} ${_outfile})
ENDFOREACH(_infile ${_pofiles})

ADD_CUSTOM_TARGET(po ALL DEPENDS ${_sources})
