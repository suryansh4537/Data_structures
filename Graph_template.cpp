#include"bits/stdc++.h"
using namespace std;

template<typename T>

class graph{


map<T,list<T> > adj;
public:

void addedge(T a,T b){
adj[a].push_back(b);
adj[b].push_back(a);
}
void displayList(){
    for(auto x:adj){
        cout<<x.first;
        for(auto y:x.second)
            cout<<"->"<<y;
        cout<<endl;
    }
}
void bfs(T s){
map<T,bool> vis;
for(auto x:adj)vis[x.first]=false;
list<T> q;
q.push_back(s);
vis[s]=true;

while(!q.empty()){
    s=q.front();
    cout<<s<< " ";
    q.pop_front();

    for(auto i=adj[s].begin();i=adj[s].end();i++){
        if(!vis[*i]){
            q.push_back(*i);
            vis[*i]=true;
        }
    }
}}

void dfsutil(map<T,bool> &vis,T s){

vis[s]=true;
cout<<s<<" ";

for(auto x: adj[s]){
    if(vis[x]==false){
        dfsutil(vis,x);
    }
}

}
void dfs(T s){
map<T,bool> vis;
for(auto x: adj)vis[x.first]=false;

dfsutil(vis,s);
}
};

int main()
{
graph<string> g;
string a,b;
for(int i=0;i<6;i++){
    cin>>a>>b;
    g.addedge(a,b);
}
g.displayList();
g.dfs("ob");
}

