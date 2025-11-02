cmake_minimum_required(VERSION 3.10)
project(keepass-sync)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(keepass-sync sync.cpp)

# Platform-specific settings
if(WIN32)
    target_link_libraries(keepass-sync)
else()
    target_link_libraries(keepass-sync)
endif()

# Installation
install(TARGETS keepass-sync
    RUNTIME DESTINATION bin
)

