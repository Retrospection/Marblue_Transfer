import Vue from 'vue'
import Router from 'vue-router'
import Query from './pages/query'
import Add from './pages/add'
import Home from './pages/home'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/query',
            name: 'query',
            component: Query
        },
        {
            path: '/add',
            name: 'add',
            component: Add
        }
    ]
})
