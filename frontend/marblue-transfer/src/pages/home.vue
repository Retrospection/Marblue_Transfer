<template>
    <div id="container">
        <div id="app">
            <header class="title">三无Marblue粉丝群换群记录</header>
            <div class="links">
                <router-link class="link" to="/query">查询记录</router-link>
                <router-link class="link" to="/add">新增记录</router-link>
            </div>
        </div>
    </div>
</template>


<style scoped>
    #container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    #app {
        display: flex;
        flex-direction: column;
        width: 960px;
        height: 600px;
    }

    .title {
        display: flex;
        justify-content: center;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 2rem;
        padding: 1rem;
        margin: 3rem 0;
    }

    .links {
        display: flex;
        flex-direction: column;

    }

    .link {
        display: flex;
        justify-content: center;
        text-decoration: none;
        font-size: 1.5rem;
        line-height: 6rem;
    }

    .link:visited {

    }


</style>
