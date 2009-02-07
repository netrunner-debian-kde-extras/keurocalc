project(doc)

add_subdirectory(da)
add_subdirectory(en)
add_subdirectory(es)
add_subdirectory(et)
add_subdirectory(fr)
add_subdirectory(it)
add_subdirectory(nb)
add_subdirectory(nl)
add_subdirectory(pt)
add_subdirectory(sv)

ADD_CUSTOM_TARGET(doc ALL DEPENDS ${_sources})
