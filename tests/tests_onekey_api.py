# -*- coding: utf-8 -*-
# @Time    : 2025/03/01

import json
import mcp_marketplace as mcpm

def run_mcp_router_api_example():
    """
        # 1. This Function Connects to Google-Maps MCPs and run maps_direction from 'Boston' to 'New York'
        # 2. Complete List of Supported Tools Use Check : https://www.deepnlp.org/doc/onekey_mcp_router
    """
    from mcp_marketplace import OneKeyMCPRouter

    example = {"server_name":"google-maps","tool_name":"maps_directions","tool_input":{"destination":"New York","mode":"driving","origin":"Boston"}}
    server_name = example.get("server_name", "")

    ## 1. MCP Initialize POST Request
    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    router = OneKeyMCPRouter(server_name=server_name, onekey=ONEKEY_BETA)

    ## 2. Check Available Tools, tools/list
    available_tools = router.tools_list(server_name)
    print (f"Server {server_name}|available_tools {available_tools}")

    ## Your LLM Code



    ## 3. Run Tool, Post tools/call request
    result_json = router.tools_call(server_name, example.get("tool_name", ""), example.get("tool_input", {}))
    print (f"Server {server_name}|tool_name {example.get("tool_name", "")} | tool_input {example.get("tool_input", {})} |result_json {result_json}")

def run_mcp_router_batch_api():
    """
    """
    from mcp_marketplace import OneKeyMCPRouter
    ## in the init router function, check if
    # 1. check if DEEPNLP_ONEKEY_ROUTER_ACCESS is set:  DEEPNLP_ONEKEY_ROUTER_ACCESS=BETA_TEST_KEY_OCT_2025
    # 2. Initilialze and post/mcp init method
    data_examples = [
        {"server_name":"google-maps","tool_name":"maps_directions","tool_input":{"destination":"北京","mode":"driving","origin":"杭州"}},
        {"server_name":"perplexity","tool_name":"perplexity_search","tool_input":{"query":"NBA News","max_results":10,"max_tokens_per_page":256,"country":"US"}}
    ]

    import time

    ONEKEY_BETA = "BETA_TEST_KEY_OCT_2025"
    mcp_routers_dict = {}
    for data_example in data_examples:
        server_name = data_example.get("server_name", "")
        mcp_routers_dict[server_name] = OneKeyMCPRouter(server_name=server_name, onekey = ONEKEY_BETA)
        # mcp_routers_dict[server_name] = OneKeyMCPRouter(server_name=server_name, onekey = ONEKEY_BETA, log_enable=True)
        print (f"INFO: OneKey MCP Router Initialize Server Connection|{server_name} ")

    for i in range(data_examples):
        data_example = data_examples[i]
        server_name = data_example.get("server_name", "")
        router = mcp_routers_dict.get(server_name)
        if router is None:
            print (f"DEBUG: server_name {server_name} is None...")
        ## 1. tools/list
        available_tools = router.tools_list(server_name)
        print (f"INFO: server_name {server_name} available tools: {available_tools}")

        ## 2. Your LLM Function Call choose tools and fill function call arguments

        ## 3. Your MCP
        tool_name = data_example.get("tool_name", "")
        tool_input = data_example.get("tool_input", {})
        ## tools/call
        result_json = router.tools_call(server_name, tool_name, tool_input)
        print(f"INFO: Server Name {server_name} | Tool Name {tool_name} | Tool Call Result {result_json}")
        ## $.result.success, $.result.content
        success = result_json.get("result", {}).get("success")
        content_list = result_json.get("result", {}).get("content")
        for content in content_list:
            print (f"Content Type {content.get('type')}")
            print (f"Content Text {content.get('text')}")

        time.sleep(1)

def main():
    """
    """

if __name__ == '__main__':
    main()
