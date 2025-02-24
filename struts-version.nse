local http = require "http"
local shortport = require "shortport"
local stdnse = require "stdnse"

description = [[
Detects if a web server is running Apache Struts and attempts to extract the version from headers, error messages, or metadata files.
]]

author = "ChatGPT"
license = "Same as Nmap--See https://nmap.org/book/man-legal.html"
categories = {"discovery", "safe"}

-- Define the ports this script should run on
portrule = shortport.http

action = function(host, port)
    local paths = { "/", "/struts/webconsole.html", "/index.action", "/login.action", "/struts2-showcase/" }
    local version_patterns = { 
        "Apache Struts ([0-9]+%.[0-9]+%.[0-9]+)",  -- Standard Struts version format
        "Struts2 ([0-9]+%.[0-9]+%.[0-9]+)",
        "Struts ([0-9]+%.[0-9]+)"
    }
    local result = {}

    for _, path in ipairs(paths) do
        local response = http.get(host, port, path)

        if response and response.status then
            -- Check headers for Struts version
            for header, value in pairs(response.header) do
                for _, pattern in ipairs(version_patterns) do
                    local version = string.match(value, pattern)
                    if version then
                        table.insert(result, "Struts version found in header: " .. header .. " = " .. version)
                    end
                end
            end

            -- Check body content for Struts version
            for _, pattern in ipairs(version_patterns) do
                if response.body then
                    local version = string.match(response.body, pattern)
                    if version then
                        table.insert(result, "Struts version found in response body at " .. path .. " -> " .. version)
                    end
                end
            end
        end
    end

    if #result > 0 then
        return stdnse.format_output(true, result)
    else
        return "No Apache Struts version detected."
    end
end
