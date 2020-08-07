from bs4 import BeautifulSoup

html_doc = """


<!doctype html>
<html lang="en">
    <head>
        <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=0, shrink-to-fit=no">
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="/common/css/bootstrap.min.css">
        <link rel="stylesheet" href="/common/fonts/iconfont.css">
        <link rel="stylesheet" href="/common/css/owl.carousel.min.css">
        <link rel="stylesheet" href="/common/css/css.css">
        <link rel="stylesheet" href="/common/css/toastr.css">

        <title>Cspiration 留学两年多刷题过三千，教你刷题不再困难；全美唯一Java版本Leetcode视频讲解</title>
    </head>
<style>
    blockquote {
        border-left:#eee solid 5px;
        padding-left:20px;
    }
    ul li {
        line-height: 20px;
    }
    code {
        color:#D34B62;
        background: #F6F6F6;
    }
    }
</style>
<body>
<header class="site-header">
    <nav class="navbar navbar-expand flex-md-row site-navbar">
        <div class="container">
            <a class="navbar-brand mr-0 mr-md-5" href="/" aria-label="Bootstrap"></a>
            <div class="navbar-nav-scroll">
                <ul class="navbar-nav bd-navbar-nav flex-row">
                    <li class="nav-item">
                        <a class="nav-link " href="/">首页</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" href="##">刷题班</a>
                        <div class="dropdown-menu dropdown-menu-left" aria-labelledby="bd-versions">
                            <a class="dropdown-item" href="/leetCodeCourse">LeetCode面试刷题班</a>
                            <a class="dropdown-item" href="/crashCourse">短期算法速成班</a>
                        </div>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" href="##">旗舰班</a>
                        <div class="dropdown-menu dropdown-menu-left" aria-labelledby="bd-versions">
                            <a class="dropdown-item" href="/course-diff">课程对比</a>
                            <a class="dropdown-item" href="/sprintCourse">北美留学SDE求职班</a>
                            <a class="dropdown-item" href="/jobCourse">北美在职SDE跳槽班</a>
                        </div>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link " href="/leetcodeClassification">LC分类顺序表</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link " href="/story">创始人故事</a>
                    </li>
                        <li class="nav-item nav-form-item">
                            <a class="nav-link" href="/login">登录</a>/
                            <a class="nav-link" href="/register">注册</a>
                        </li>
                </ul>
            </div>
        </div>
    </nav>
</header>
<div class="cert-banner" style="background-image: url(/common/images/cat_banner.jpg);">
    <div class="cert-text">Leetcode 分类顺序表</div>
</div>
<div class="inwrap" style="padding-top: 40px;">
    <div class="container leet-container">
        <div class="row">
            <div class="sidebar">
                <div class="side-panel">
                    <ul class="nav nav-tabs side-navbar" role="tablist" id="">
                        <li>
                            <a class="nav-link active" id="nav-jieshao-tab" data-toggle="tab" href="#nav-jieshao" role="tab" aria-controls="nav-jieshao"
                               aria-selected="true">介绍</a>
                        </li>
                        <li>
                            <div class="tab-cell">
                                <a class="nav-link" data-toggle="tab" role="tab"  href="javascript:;">Leetcode 分类顺序表</a>
                                <span class="down-icon"></span>
                            </div>
                            <ul class="nav nav-tabs sec-navbar" role="tablist">
                                <li class="">
                                    <a class="nav-link" id="nav-Array-tab" data-toggle="tab" href="#nav-Array" role="tab" aria-controls="nav-Array"
                                       aria-selected="false">Array</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-String-tab" data-toggle="tab" href="#nav-String" role="tab" aria-controls="nav-String"
                                       aria-selected="false">String</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-Math-tab" data-toggle="tab" href="#nav-Math" role="tab" aria-controls="nav-Math"
                                       aria-selected="false">Math</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-Tree-tab" data-toggle="tab" href="#nav-Tree" role="tab" aria-controls="nav-Tree"
                                       aria-selected="false">Tree</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-Backtracking-tab" data-toggle="tab" href="#nav-Backtracking" role="tab" aria-controls="nav-Backtracking"
                                       aria-selected="false">Backtracking</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-DynamicProgramming-tab" data-toggle="tab" href="#nav-DynamicProgramming" role="tab" aria-controls="nav-DynamicProgramming"
                                       aria-selected="false">Dynamic Programming</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-LinkedList-tab" data-toggle="tab" href="#nav-LinkedList" role="tab" aria-controls="nav-LinkedList"
                                       aria-selected="false">LinkedList</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-BinarySearch-tab" data-toggle="tab" href="#nav-BinarySearch" role="tab" aria-controls="nav-BinarySearch"
                                       aria-selected="false">Binary Search</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-Matrix-tab" data-toggle="tab" href="#nav-Matrix" role="tab" aria-controls="nav-Matrix"
                                       aria-selected="false">Matrix</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-DFSBFS-tab" data-toggle="tab" href="#nav-DFSBFS" role="tab" aria-controls="nav-DFSBFS"
                                       aria-selected="false">DFS & BFS</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-StackPriorityQueue-tab" data-toggle="tab" href="#nav-StackPriorityQueue" role="tab" aria-controls="nav-StackPriorityQueue"
                                       aria-selected="false">Stack & PriorityQueue</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-BitManipulation-tab" data-toggle="tab" href="#nav-BitManipulation" role="tab" aria-controls="nav-BitManipulation"
                                       aria-selected="false">Bit Manipulation</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-TopologicalSort-tab" data-toggle="tab" href="#nav-TopologicalSort" role="tab" aria-controls="nav-TopologicalSort"
                                       aria-selected="false">Topological Sort</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-Random-tab" data-toggle="tab" href="#nav-Random" role="tab" aria-controls="nav-Random"
                                       aria-selected="false">Random</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-Graph-tab" data-toggle="tab" href="#nav-Graph" role="tab" aria-controls="nav-Graph"
                                       aria-selected="false">Graph</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-UnionFind-tab" data-toggle="tab" href="#nav-UnionFind" role="tab" aria-controls="nav-UnionFind"
                                       aria-selected="false">Union Find</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-Trie-tab" data-toggle="tab" href="#nav-Trie" role="tab" aria-controls="nav-Trie"
                                       aria-selected="false">Trie</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-Design-tab" data-toggle="tab" href="#nav-Design" role="tab" aria-controls="nav-Design"
                                       aria-selected="false">Design</a>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <div class="tab-cell">
                                <a class="nav-link" data-toggle="tab" role="tab"  href="javascript:;">Leetcode 重点250题</a>
                                <span class="down-icon"></span>
                            </div>
                            <ul class="nav nav-tabs sec-navbar" role="tablist">
                                <li class="">
                                    <a class="nav-link" id="nav-huafenshuoming-tab" data-toggle="tab" href="#nav-huafenshuoming" role="tab" aria-controls="nav-huafenshuoming"
                                       aria-selected="false">划分说明</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-zhongdiantimu-tab" data-toggle="tab" href="#nav-zhongdiantimu" role="tab" aria-controls="nav-zhongdiantimu"
                                       aria-selected="false">重点250题</a>
                                </li>
                            </ul>
                        </li>
                        <li>
                                <div class="tab-cell">
                                    <a class="nav-link" data-toggle="tab" role="tab"  href="javascript:;">Data Science Leetcode精简版</a>
                                    <span class="down-icon"></span>
                                </div>
                                <ul class="nav nav-tabs sec-navbar" role="tablist">
                                    <li class="">
                                        <a class="nav-link" id="nav-DShuafenshuoming-tab" data-toggle="tab" href="#nav-DShuafenshuoming" role="tab" aria-controls="nav-DShuafenshuoming"
                                           aria-selected="false">划分说明</a>
                                    </li>
                                    <li class="">
                                        <a class="nav-link" id="nav-DSzhongdiantimu-tab" data-toggle="tab" href="#nav-DSzhongdiantimu" role="tab" aria-controls="nav-DSzhongdiantimu"
                                           aria-selected="false">精简题目</a>
                                    </li>
                                </ul>
                            </li>
                        <li>
                            <div class="tab-cell">
                                <a class="nav-link" data-toggle="tab" role="tab"  href="javascript:;">刷题常见问题</a>
                                <span class="down-icon"></span>
                            </div>
                            <ul class="nav nav-tabs sec-navbar" role="tablist">
                                <li class="">
                                    <a class="nav-link" id="nav-question1-tab" data-toggle="tab" href="#nav-question1" role="tab" aria-controls="nav-question1"
                                       aria-selected="false">分类顺序表400题够吗</a>
                                </li>
                                <li class="">
                                    <a class="nav-link" id="nav-question2-tab" data-toggle="tab" href="#nav-question2" role="tab" aria-controls="nav-question2"
                                       aria-selected="false">我想提问题</a>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <a class="nav-link" id="nav-about-tab" data-toggle="tab" href="#nav-about" role="tab" aria-controls="nav-about"
                               aria-selected="false">关于作者</a>
                        </li>
                        <li>
                            <a class="nav-link" id="weixinjiaoliuqun" data-toggle="tab" href="#nav-weixinjiaoliuqun" role="tab" aria-controls="nav-weixinjiaoliuqun"
                               aria-selected="false">微信交流群</a>
                        </li>
                        <li>
                            <a class="nav-link" id="cankaowangzhan" data-toggle="tab" href="#nav-cankaowangzhan" role="tab" aria-controls="nav-cankaowangzhan"
                               aria-selected="false">参考网站</a>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="col-main">
                <div class="inner">
                    <div class="tab-content" id="nav-tabContent">
                        <div class="tab-pane fade show active" id="nav-jieshao" role="tabpanel" aria-labelledby="nav-jieshao-tab">
                            <div class="col-panel">
                                <div class="col-header">致所有使用者</div>
                                <div class="col-body">
                                    <div class="col-cell">
                                        <div class="cell-header">
                                            <i class="iconfont icon-kecheng"></i> <strong>Cspiration 独家出品</strong>
                                        </div>
                                        <div class="cell-body">
                                            此表以先易后难 + 分类而成。Leetcode（https://leetcode.com/）本身并没有顺序，
                                            并且类别分的并不是非常好，因为大量非最优解也涵盖在各种类别中。
                                            所以我们依据做题经验，最优解的类别，难度，重新划分。
                                            如果是第一次刷题的小伙伴，最好以本书的顺序为主，可以为大家节省时间，更有效率的做题，减少很多刷题的负担。
                                        </div>
                                    </div>
                                    <div class="col-cell">
                                        <div class="cell-body">
                                            注：本表非最终版本。《题型技巧总结》课程中有最终Leetcode分类顺序表版本，更细致，每种题目对应方法一并写出，
                                            并且同类型做题方法归纳一起。
                                        </div>
                                    </div>
                                    <div class="row row-wx">
                                        <div class="col-lg-4">
                                            <div class="col-wx">
                                                <img src="/common/images/小助手.png" height="150px" width="150px" alt="" />
                                                <p>-北美CS刷题求职群-<br /><span>实习全职百人大群</span></p>
                                            </div>
                                        </div>
                                        <div class="col-lg-4">
                                            <div class="col-wx">
                                                <img src="/common/images/Cspiration服务号.jpg" height="150px" width="150px" alt="" />
                                                <p>-Cspiration官方公众号-<br/><span>每周第一手求职信息</span></p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
<!--Array-->
<div class="tab-pane fade" id="nav-Array" role="tabpanel" aria-labelledby="nav-Array">
    <div class="col-panel">
        <div class="col-header">Array</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                    <td>说明</td>
                </tr>
                </thead>
                <tbody>
                <tr>
    <td>基础</td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>27</td>
    <td><a href="https://leetcode.com/problems/remove-element/"
           target="_blank" class="text-link">Remove Element</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>

    <td></td>
</tr>
<tr>
    <td>26</td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/"
           target="_blank" class="text-link">Remove Duplicates from Sorted Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>80</td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/"
           target="_blank" class="text-link">Remove Duplicates from Sorted Array II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>277</td>
    <td><a href="https://leetcode.com/problems/find-the-celebrity/description/"
           target="_blank" class="text-link">Find the Celebrity</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>189</td>
    <td><a href="https://leetcode.com/problems/rotate-array/description/"
           target="_blank" class="text-link">Rotate Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>41</td>
    <td><a href="https://leetcode.com/problems/first-missing-positive/description/"
           target="_blank" class="text-link">First Missing Positive</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>299</td>
    <td><a href="https://leetcode.com/problems/bulls-and-cows/"
           target="_blank" class="text-link">Bulls and Cows</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>134</td>
    <td><a href="https://leetcode.com/problems/gas-station/description/"
           target="_blank" class="text-link">Gas Station</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>118</td>
    <td><a href="https://leetcode.com/problems/pascals-triangle/description/" 
           target="_blank" class="text-link">Pascal's Triangle</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>119</td>
    <td><a href="https://leetcode.com/problems/pascals-triangle-ii/description/" 
           target="_blank" class="text-link">Pascal's Triangle II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>169</td>
    <td><a href="https://leetcode.com/problems/majority-element/description/" 
           target="_blank" class="text-link">Majority Element</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>229</td>
    <td><a href="https://leetcode.com/problems/majority-element-ii/description/" 
           target="_blank" class="text-link">Majority Element II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>274</td>
    <td><a href="https://leetcode.com/problems/h-index/description/"
           target="_blank" class="text-link">H-Index</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>275</td>
    <td><a href="https://leetcode.com/problems/h-index-ii/description/"
           target="_blank" class="text-link">H-Index II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>Binary Search</td>
</tr>
<tr>
    <td>243</td>
    <td><a href="https://leetcode.com/problems/shortest-word-distance/description/" 
           target="_blank" class="text-link">Shortest Word Distance</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>244</td>
    <td><a href="https://leetcode.com/problems/shortest-word-distance-ii/description/"
           target="_blank" class="text-link">Shortest Word Distance II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>245</td>
    <td><a href="https://leetcode.com/problems/shortest-word-distance-iii/description/" target="_blank" class="text-link">Shortest Word Distance III</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>217</td>
    <td><a href="https://leetcode.com/problems/contains-duplicate/description/"
               target="_blank" class="text-link">Contains Duplicate</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>219</td>
    <td><a href="https://leetcode.com/problems/contains-duplicate-ii/description/"
           target="_blank" class="text-link">Contains Duplicate II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>220</td>
    <td><a href="https://leetcode.com/problems/contains-duplicate-iii/description/"
           target="_blank" class="text-link">Contains Duplicate III</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>55</td>
    <td><a href="https://leetcode.com/problems/jump-game/description/"
           target="_blank" class="text-link">Jump Game</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>45</td>
    <td><a href="https://leetcode.com/problems/jump-game-ii/description/"
           target="_blank" class="text-link">Jump Game II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>121</td>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/"
           target="_blank" class="text-link">Best Time to Buy and Sell Stock</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>122</td>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/"
           target="_blank" class="text-link"> Best Time to Buy and Sell Stock II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>123</td>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/"
           target="_blank" class="text-link">Best Time to Buy and Sell Stock III</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>188</td>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/"
           target="_blank" class="text-link">Best Time to Buy and Sell Stock IV</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>309</td>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/"
           target="_blank" class="text-link">Best Time to Buy and Sell Stock with Cooldown</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>11</td>
    <td><a href="https://leetcode.com/problems/container-with-most-water/description/"
           target="_blank" class="text-link">Container With Most Water</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>42</td>
    <td><a href="https://leetcode.com/problems/trapping-rain-water/description/"
           target="_blank" class="text-link">Trapping Rain Water</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>334</td>
    <td><a href="https://leetcode.com/problems/increasing-triplet-subsequence/description/"
           target="_blank" class="text-link">Increasing Triplet Subsequence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>128</td>
    <td><a href="https://leetcode.com/problems/longest-consecutive-sequence/description/"
           target="_blank" class="text-link">Longest Consecutive Sequence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>164</td>
    <td><a href="https://leetcode.com/problems/maximum-gap/description/" 
           target="_blank" class="text-link">Maximum Gap</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>Bucket</td>
</tr>
<tr>
    <td>287</td>
    <td><a href="https://leetcode.com/problems/find-the-duplicate-number/description/"
           target="_blank" class="text-link">Find the Duplicate Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>135</td>
    <td><a href="https://leetcode.com/problems/candy/description/" 
           target="_blank" class="text-link">Candy</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>330</td>
    <td><a href="https://leetcode.com/problems/patching-array/description/" 
           target="_blank" class="text-link">Patching Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>提高</td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>4</td>
    <td><a href="https://leetcode.com/problems/median-of-two-sorted-arrays/description/"
           target="_blank" class="text-link">Median of Two Sorted Arrays</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>321</td>
    <td><a href="https://leetcode.com/problems/create-maximum-number/description/"
           target="_blank" class="text-link">Create Maximum Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>327</td>
    <td><a href="https://leetcode.com/problems/count-of-range-sum/description/"
           target="_blank" class="text-link">Count of Range Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>289</td>
    <td><a href="https://leetcode.com/problems/game-of-life/description/"
           target="_blank" class="text-link">Game of Life</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>Interval</td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>57</td>
    <td><a href="https://leetcode.com/problems/insert-interval/description/"
           target="_blank" class="text-link">Insert Interval</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>56</td>
    <td><a href="https://leetcode.com/problems/merge-intervals/description/"
           target="_blank" class="text-link">Merge Intervals</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>252</td>
    <td><a href="https://leetcode.com/problems/meeting-rooms/description/"
           target="_blank" class="text-link">Meeting Rooms</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>253</td>
    <td><a href="https://leetcode.com/problems/meeting-rooms-ii/description/"
           target="_blank" class="text-link">Meeting Rooms II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>352</td>
    <td><a href="https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/"
           target="_blank" class="text-link">Data Stream as Disjoint Intervals</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>TreeMap</td>
</tr>

<tr>
    <td>Counter</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>239</td>
    <td><a href="https://leetcode.com/problems/sliding-window-maximum/description/"
           target="_blank" class="text-link">Sliding Window Maximum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>295</td>
    <td><a href="https://leetcode.com/problems/find-median-from-data-stream/description/"
           target="_blank" class="text-link">Find Median from Data Stream</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>53</td>
    <td><a href="https://leetcode.com/problems/maximum-subarray/description/"
           target="_blank" class="text-link">Maximum Subarray</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>325</td>
    <td><a href="https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/"
           target="_blank" class="text-link">Maximum Size Subarray Sum Equals k</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>209</td>
    <td><a href="https://leetcode.com/problems/minimum-size-subarray-sum/description/"
           target="_blank" class="text-link">Minimum Size Subarray Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>238</td>
    <td><a href="https://leetcode.com/problems/product-of-array-except-self/description/"
           target="_blank" class="text-link">Product of Array Except Self</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>152</td>
    <td><a href="https://leetcode.com/problems/maximum-product-subarray/description/"
           target="_blank" class="text-link">Maximum Product Subarray</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>228</td>
    <td><a href="https://leetcode.com/problems/summary-ranges/description/"
           target="_blank" class="text-link">Summary Ranges</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>163</td>
    <td><a href="https://leetcode.com/problems/missing-ranges/description/"
           target="_blank" class="text-link">Missing Ranges</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>Counter</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>88</td>
    <td><a href="https://leetcode.com/problems/merge-sorted-array/description/"
           target="_blank" class="text-link">Merge Sorted Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>75</td>
    <td><a href="https://leetcode.com/problems/sort-colors/description/"
           target="_blank" class="text-link">Sort Colors</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>283</td>
    <td><a href="https://leetcode.com/problems/move-zeroes/description/"
           target="_blank" class="text-link">Move Zeroes</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>376</td>
    <td><a href="https://leetcode.com/problems/wiggle-subsequence/description/"
           target="_blank" class="text-link">Wiggle Subsequence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>280</td>
    <td><a href="https://leetcode.com/problems/wiggle-sort/description/"
           target="_blank" class="text-link">Wiggle Sort</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>324</td>
    <td><a href="https://leetcode.com/problems/wiggle-sort-ii/description/"
           target="_blank" class="text-link"> Wiggle Sort II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>278</td>
    <td><a href="https://leetcode.com/problems/first-bad-version/description/"
           target="_blank" class="text-link"> First Bad Version</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>35</td>
    <td><a href="https://leetcode.com/problems/search-insert-position/description/"
           target="_blank" class="text-link">Search Insert Position</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>33</td>
    <td><a href="https://leetcode.com/problems/search-in-rotated-sorted-array/description/"
           target="_blank" class="text-link">Search in Rotated Sorted Array</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>81</td>
    <td><a href="https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/"
           target="_blank" class="text-link">Search in Rotated Sorted Array II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>153</td>
    <td><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/"
           target="_blank" class="text-link">Find Minimum in Rotated Sorted Array</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>154</td>
    <td><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/"
           target="_blank" class="text-link">Find Minimum in Rotated Sorted Array II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>162</td>
    <td><a href="https://leetcode.com/problems/find-peak-element/description/"
           target="_blank" class="text-link">Find Peak Element </a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>374</td>
    <td><a href="https://leetcode.com/problems/guess-number-higher-or-lower/"
           target="_blank" class="text-link">Guess Number Higher or Lower</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>34</td>
    <td><a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/"
           target="_blank" class="text-link"> Find First and Last Position of Element in Sorted Array
    </a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>349</td>
    <td><a href="https://leetcode.com/problems/intersection-of-two-arrays/description/"
           target="_blank" class="text-link">Intersection of Two Arrays</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>350</td>
    <td><a href="https://leetcode.com/problems/intersection-of-two-arrays-ii/description/"
           target="_blank" class="text-link">Intersection of Two Arrays II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>315</td>
    <td><a href="https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/"
           target="_blank" class="text-link">Count of Smaller Numbers After Self</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>300</td>
    <td><a href="https://leetcode.com/problems/longest-increasing-subsequence/description/"
           target="_blank" class="text-link">Longest Increasing Subsequence</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>354</td>
    <td><a href="https://leetcode.com/problems/russian-doll-envelopes/description/"
           target="_blank" class="text-link">Russian Doll Envelopes</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--String-->
<div class="tab-pane fade" id="nav-String" role="tabpanel" aria-labelledby="nav-String">
    <div class="col-panel">
        <div class="col-header">String</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                    <td>说明</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>基础</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>28</td>
    <td><a href="https://leetcode.com/problems/implement-strstr/description/"
           target="_blank" class="text-link">Implement strStr()</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>14</td>
    <td><a href="https://leetcode.com/problems/longest-common-prefix/description/" 
           target="_blank" class="text-link">Longest Common Prefix</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>58</td>
    <td><a href="https://leetcode.com/problems/length-of-last-word/description/"
           target="_blank" class="text-link">Length of Last Word</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>387</td>
    <td><a href="https://leetcode.com/problems/first-unique-character-in-a-string/description/"
           target="_blank" class="text-link">First Unique Character in a String</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>383</td>
    <td><a href="https://leetcode.com/problems/ransom-note/description/"
           target="_blank" class="text-link">Ransom Note</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>344</td>
    <td><a href="https://leetcode.com/problems/reverse-string/description/"
           target="_blank" class="text-link">Reverse String</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>151</td>
    <td><a href="https://leetcode.com/problems/reverse-words-in-a-string/description/"
           target="_blank" class="text-link">Reverse Words in a String</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>186</td>
    <td><a href="https://leetcode.com/problems/reverse-words-in-a-string-ii/description/"
           target="_blank" class="text-link">Reverse Words in a String II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>345</td>
    <td><a href="https://leetcode.com/problems/reverse-vowels-of-a-string/description/"
           target="_blank" class="text-link">Reverse Vowels of a String</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>205</td>
    <td><a href="https://leetcode.com/problems/isomorphic-strings/description/"
           target="_blank" class="text-link">Isomorphic Strings</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>293</td>
    <td><a href="https://leetcode.com/problems/flip-game/description/"
           target="_blank" class="text-link">Flip Game</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>294</td>
    <td><a href="https://leetcode.com/problems/flip-game-ii/description/"
           target="_blank" class="text-link">Flip Game II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>290</td>
    <td><a href="https://leetcode.com/problems/word-pattern/description/"
           target="_blank" class="text-link">Word Pattern</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>242</td>
    <td><a href="https://leetcode.com/problems/valid-anagram/description/"
           target="_blank" class="text-link">Valid Anagram</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>49</td>
    <td><a href="https://leetcode.com/problems/group-anagrams/description/"
           target="_blank" class="text-link">Group Anagrams</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>249</td>
    <td><a href="https://leetcode.com/problems/group-shifted-strings/description/"
           target="_blank" class="text-link">Group Shifted Strings</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>87</td>
    <td><a href="https://leetcode.com/problems/scramble-string/description/"
           target="_blank" class="text-link">Scramble String</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>179</td>
    <td><a href="https://leetcode.com/problems/largest-number/description/"
           target="_blank" class="text-link">Largest Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>6</td>
    <td><a href="https://leetcode.com/problems/zigzag-conversion/description/"
           target="_blank" class="text-link">ZigZag Conversion</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>161</td>
    <td><a href="https://leetcode.com/problems/one-edit-distance/"
           target="_blank" class="text-link">One Edit Distance</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>38</td>
    <td><a href="https://leetcode.com/problems/count-and-say/description/"
           target="_blank" class="text-link">Count and Say</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>358</td>
    <td><a href="https://leetcode.com/problems/rearrange-string-k-distance-apart/description/"
           target="_blank" class="text-link">Rearrange String k Distance Apart</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>316</td>
    <td><a href="https://leetcode.com/problems/remove-duplicate-letters/description/"
           target="_blank" class="text-link">Remove Duplicate Letters</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>271</td>
    <td><a href="https://leetcode.com/problems/encode-and-decode-strings/description/"
           target="_blank" class="text-link">Encode and Decode Strings</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>168</td>
    <td><a href="https://leetcode.com/problems/excel-sheet-column-title/description/"
           target="_blank" class="text-link">Excel Sheet Column Title</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>171</td>
    <td><a href="https://leetcode.com/problems/excel-sheet-column-number/description/"
           target="_blank" class="text-link">Excel Sheet Column Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>13</td>
    <td><a href="https://leetcode.com/problems/roman-to-integer/description/"
           target="_blank" class="text-link">Roman to Integer</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>12</td>
    <td><a href="https://leetcode.com/problems/integer-to-roman/description/"
           target="_blank" class="text-link">Integer to Roman</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>273</td>
    <td><a href="https://leetcode.com/problems/integer-to-english-words/description/"
           target="_blank" class="text-link">Integer to English Words</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>246</td>
    <td><a href="https://leetcode.com/problems/strobogrammatic-number/description/"
           target="_blank" class="text-link">Strobogrammatic Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>247</td>
    <td><a href="https://leetcode.com/problems/strobogrammatic-number-ii/description/"
           target="_blank" class="text-link">Strobogrammatic Number II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>248</td>
    <td><a href="https://leetcode.com/problems/strobogrammatic-number-iii/description/"
           target="_blank" class="text-link">Strobogrammatic Number III</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>

<tr>
    <td>提高</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>157</td>
    <td><a href="https://leetcode.com/problems/read-n-characters-given-read4/description/"
           target="_blank" class="text-link">Read N Characters Given Read4</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>158</td>
    <td><a href="https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/description/"
           target="_blank" class="text-link">Read N Characters Given Read4 II - Call multiple times</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>68</td>
    <td><a href="https://leetcode.com/problems/text-justification/description/"
           target="_blank" class="text-link">Text Justification</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>65</td>
    <td><a href="https://leetcode.com/problems/valid-number/description/"
           target="_blank" class="text-link">Valid Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>Substring</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>76</td>
    <td><a href="https://leetcode.com/problems/minimum-window-substring/description/"
           target="_blank" class="text-link">Minimum Window Substring</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>Sliding Window</td>
</tr>
<tr>
    <td>30</td>
    <td><a href="https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/"
           target="_blank" class="text-link">Substring with Concatenation of All Words
    </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>Sliding Window</td>
</tr>
<tr>
    <td>3</td>
    <td><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/description/"
           target="_blank" class="text-link">Longest Substring Without Repeating Characters</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>Sliding Window</td>
</tr>
<tr>
    <td>340</td>
    <td><a href="https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/"
           target="_blank" class="text-link">Longest Substring with At Most K Distinct Characters</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>Sliding Window</td>
</tr>
<tr>
    <td>395</td>
    <td><a href="https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/"
           target="_blank" class="text-link"> Longest Substring with At Least K Repeating Characters</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>Sliding Window</td>
</tr>
<tr>
    <td>159</td>
    <td><a href="https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/"
           target="_blank" class="text-link">Longest Substring with At Most Two Distinct Characters</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>Sliding Window</td>
</tr>

<tr>
    <td>Palindrome</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>125</td>
    <td><a href="https://leetcode.com/problems/valid-palindrome/description/"
           target="_blank" class="text-link">Valid Palindrome</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>266</td>
    <td><a href="https://leetcode.com/problems/palindrome-permutation/description/"
           target="_blank" class="text-link">Palindrome Permutation</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>5</td>
    <td><a href="https://leetcode.com/problems/longest-palindromic-substring/description/"
           target="_blank" class="text-link">Longest Palindromic Substring
    </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>9</td>
    <td><a href="https://leetcode.com/problems/palindrome-number/description/" target="_blank"
           class="text-link">Palindrome Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>214</td>
    <td><a href="https://leetcode.com/problems/shortest-palindrome/description/"
           target="_blank" class="text-link">Shortest Palindrome</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>336</td>
    <td><a href="https://leetcode.com/problems/palindrome-pairs/description/"
           target="_blank" class="text-link">Palindrome Pairs</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>131</td>
    <td><a href="https://leetcode.com/problems/palindrome-partitioning/description/"
           target="_blank" class="text-link">Palindrome Partitioning</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>132</td>
    <td><a href="https://leetcode.com/problems/palindrome-partitioning-ii/description/"
           target="_blank" class="text-link">Palindrome Partitioning II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>267</td>
    <td><a href="https://leetcode.com/problems/palindrome-permutation-ii/description/"
           target="_blank" class="text-link">Palindrome Permutation II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>Parentheses</td>
    <td></td>
    <td></td>
    <td></td>
</tr>


<tr>
    <td>20</td>
    <td><a href="https://leetcode.com/problems/valid-parentheses/description/"
           target="_blank" class="text-link">Valid Parentheses</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>22</td>
    <td><a href="https://leetcode.com/problems/generate-parentheses/description/"
           target="_blank" class="text-link">Generate Parentheses</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>32</td>
    <td><a href="https://leetcode.com/problems/longest-valid-parentheses/description/"
           target="_blank" class="text-link">Longest Valid Parentheses</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>241</td>
    <td><a href="https://leetcode.com/problems/different-ways-to-add-parentheses/description/"
           target="_blank" class="text-link"> Different Ways to Add Parentheses</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>301</td>
    <td><a href="https://leetcode.com/problems/remove-invalid-parentheses/description/"
           target="_blank" class="text-link">Remove Invalid Parentheses</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>Subsequence</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>392</td>
    <td><a href="https://leetcode.com/problems/is-subsequence/description/"
           target="_blank" class="text-link">Is Subsequence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>115</td>
    <td><a href="https://leetcode.com/problems/distinct-subsequences/description/"
           target="_blank" class="text-link">Distinct Subsequences</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>187</td>
    <td><a href="https://leetcode.com/problems/repeated-dna-sequences/description/"
           target="_blank" class="text-link">Repeated DNA Sequences</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--Math-->
<div class="tab-pane fade" id="nav-Math" role="tabpanel" aria-labelledby="nav-Math">
    <div class="col-panel">
        <div class="col-header">Math</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                    <td>说明</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>基础</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>7</td>
    <td><a href="https://leetcode.com/problems/reverse-integer/description/"
           target="_blank" class="text-link">Reverse Integer</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>165</td>
    <td><a href="https://leetcode.com/problems/compare-version-numbers/description/" 
           target="_blank" class="text-link">Compare Version Numbers</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>66</td>
    <td><a href="https://leetcode.com/problems/plus-one/description/"
           target="_blank" class="text-link">Plus One</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>8</td>
    <td><a href="https://leetcode.com/problems/string-to-integer-atoi/description/"
           target="_blank" class="text-link">String to Integer (atoi)</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>258</td>
    <td><a href="https://leetcode.com/problems/add-digits/description/" 
           target="_blank" class="text-link"> Add Digits</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>67</td>
    <td><a href="https://leetcode.com/problems/add-binary/description/"
           target="_blank" class="text-link">Add Binary</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>43</td>
    <td><a href="https://leetcode.com/problems/multiply-strings/description/"
           target="_blank" class="text-link">Multiply Strings</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>29</td>
    <td><a href="https://leetcode.com/problems/divide-two-integers/description/"
           target="_blank" class="text-link">Divide Two Integers</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>69</td>
    <td><a href="https://leetcode.com/problems/sqrtx/description/"
           target="_blank" class="text-link">Sqrt(x)</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>50</td>
    <td><a href="https://leetcode.com/problems/powx-n/description/" target="_blank"
           class="text-link">Pow(x, n)</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>367</td>
    <td><a href="https://leetcode.com/problems/valid-perfect-square/description/"
           target="_blank" class="text-link">Valid Perfect Square</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>365</td>
    <td><a href="https://leetcode.com/problems/water-and-jug-problem/description/" 
           target="_blank" class="text-link">Water and Jug Problem</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>204</td>
    <td><a href="https://leetcode.com/problems/count-primes/description/"
           target="_blank" class="text-link">Count Primes</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>Sum</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>1</td>
    <td><a href="https://leetcode.com/problems/two-sum/description/"
           target="_blank" class="text-link">Two Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>167</td>
    <td><a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/" 
           target="_blank" class="text-link">Two Sum II - Input array is sorted</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>15</td>
    <td><a href="https://leetcode.com/problems/3sum/description/"
           target="_blank" class="text-link">3Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>16</td>
    <td><a href="https://leetcode.com/problems/3sum-closest/description/" 
           target="_blank" class="text-link">3Sum Closest</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>259</td>
    <td><a href="https://leetcode.com/problems/3sum-smaller/description/" 
           target="_blank" class="text-link">3Sum Smaller</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>18</td>
    <td><a href="https://leetcode.com/problems/4sum/description/"
           target="_blank" class="text-link">4Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>很少考</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>231</td>
    <td><a href="https://leetcode.com/problems/power-of-two/description/"
           target="_blank" class="text-link">Power of Two</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>326</td>
    <td><a href="https://leetcode.com/problems/power-of-three/description/"
           target="_blank" class="text-link"> Power of Three</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>342</td>
    <td><a href="https://leetcode.com/problems/power-of-four/description/"
           target="_blank" class="text-link">Power of Four</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>372</td>
    <td><a href="https://leetcode.com/problems/super-pow/description/"
           target="_blank" class="text-link">Super Pow</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>233</td>
    <td><a href="https://leetcode.com/problems/number-of-digit-one/description/"
           target="_blank" class="text-link">Number of Digit One</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>319</td>
    <td><a href="https://leetcode.com/problems/bulb-switcher/description/"
           target="_blank" class="text-link">Bulb Switcher</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>292</td>
    <td><a href="https://leetcode.com/problems/nim-game/description/"
           target="_blank" class="text-link"> Nim Game</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>202</td>
    <td><a href="https://leetcode.com/problems/happy-number/description/"
           target="_blank" class="text-link">Happy Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>400</td>
    <td><a href="https://leetcode.com/problems/nth-digit/description/"
           target="_blank" class="text-link">Nth Digit</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>263</td>
    <td><a href="https://leetcode.com/problems/ugly-number/description/"
           target="_blank" class="text-link">Ugly Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>264</td>
    <td><a href="https://leetcode.com/problems/ugly-number-ii/description/"
           target="_blank" class="text-link">Ugly Number II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>306</td>
    <td><a href="https://leetcode.com/problems/additive-number/description/"
           target="_blank" class="text-link">Additive Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>172</td>
    <td><a href="https://leetcode.com/problems/factorial-trailing-zeroes/description/"
           target="_blank" class="text-link">Factorial Trailing Zeroes</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>343</td>
    <td><a href="https://leetcode.com/problems/integer-break/description/"
           target="_blank" class="text-link">Integer Break</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>396</td>
    <td><a href="https://leetcode.com/problems/rotate-function/description/"
           target="_blank" class="text-link">Rotate Function</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>390</td>
    <td><a href="https://leetcode.com/problems/elimination-game/description/"
           target="_blank" class="text-link">Elimination Game</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>386</td>
    <td><a href="https://leetcode.com/problems/lexicographical-numbers/description/"
           target="_blank" class="text-link">Lexicographical Numbers</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>357</td>
    <td><a href="https://leetcode.com/problems/count-numbers-with-unique-digits/description/"
           target="_blank" class="text-link">Count Numbers with Unique Digits</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>360</td>
    <td><a href="https://leetcode.com/problems/sort-transformed-array/description/"
           target="_blank" class="text-link">Sort Transformed Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>397</td>
    <td><a href="https://leetcode.com/problems/integer-replacement/description/"
           target="_blank" class="text-link">Integer Replacement</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>368</td>
    <td><a href="https://leetcode.com/problems/largest-divisible-subset/description/"
           target="_blank" class="text-link">Largest Divisible Subset</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--Tree-->
<div class="tab-pane fade" id="nav-Tree" role="tabpanel" aria-labelledby="nav-Tree">
    <div class="col-panel">
        <div class="col-header">Tree</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                    <td>说明</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>基础</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>144</td>
    <td><a href="https://leetcode.com/problems/binary-tree-preorder-traversal/description/"
           target="_blank" class="text-link">Binary Tree Preorder Traversal</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>94</td>
    <td><a href="https://leetcode.com/problems/binary-tree-inorder-traversal/description/"
           target="_blank" class="text-link">Binary Tree Inorder Traversal</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>145</td>
    <td><a href="https://leetcode.com/problems/binary-tree-postorder-traversal/description/"
           target="_blank" class="text-link">Binary Tree Postorder Traversal</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>102</td>
    <td><a href="https://leetcode.com/problems/binary-tree-level-order-traversal/description/"
           target="_blank" class="text-link">Binary Tree Level Order Traversal</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>Preorder</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>100</td>
    <td><a href="https://leetcode.com/problems/same-tree/description/"
           target="_blank" class="text-link">Same Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>101</td>
    <td><a href="https://leetcode.com/problems/symmetric-tree/description/"
           target="_blank" class="text-link">Symmetric Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>226</td>
    <td><a href="https://leetcode.com/problems/invert-binary-tree/description/"
           target="_blank" class="text-link">Invert Binary Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>preorder + BFS</td>
</tr>
<tr>
    <td>257</td>
    <td><a href="https://leetcode.com/problems/binary-tree-paths/description/"
           target="_blank" class="text-link">Binary Tree Paths</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>112</td>
    <td><a href="https://leetcode.com/problems/path-sum/description/" target="_blank" class="text-link">Path Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>113</td>
    <td><a href="https://leetcode.com/problems/path-sum-ii/description/"
           target="_blank" class="text-link">Path Sum II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>129</td>
    <td><a href="https://leetcode.com/problems/sum-root-to-leaf-numbers/description/"
           target="_blank" class="text-link">Sum Root to Leaf Numbers</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>298</td>
    <td><a href="https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/"
           target="_blank" class="text-link">Binary Tree Longest Consecutive Sequence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>111</td>
    <td><a href="https://leetcode.com/problems/minimum-depth-of-binary-tree/description/"
           target="_blank" class="text-link">Minimum Depth of Binary Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>Preorder</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>104</td>
    <td><a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/description/"
           target="_blank" class="text-link">Maximum Depth of Binary Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>110</td>
    <td><a href="https://leetcode.com/problems/balanced-binary-tree/description/"
           target="_blank" class="text-link">Balanced Binary Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>124</td>
    <td><a href="https://leetcode.com/problems/binary-tree-maximum-path-sum/description/"
           target="_blank" class="text-link">Binary Tree Maximum Path Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>250</td>
    <td><a href="https://leetcode.com/problems/count-univalue-subtrees/description/"
           target="_blank" class="text-link">Count Univalue Subtrees</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>366</td>
    <td><a href="https://leetcode.com/problems/find-leaves-of-binary-tree/description/"
           target="_blank" class="text-link">Find Leaves of Binary Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>337</td>
    <td><a href="https://leetcode.com/problems/house-robber-iii/description/"
           target="_blank" class="text-link">House Robber III</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>postorder + preorder</td>
</tr>

<tr>
    <td>BFS</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>107</td>
    <td><a href="https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/"
           target="_blank" class="text-link">Binary Tree Level Order Traversal II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>103</td>
    <td><a href="https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/"
           target="_blank" class="text-link">Binary Tree Zigzag Level Order Traversal</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>199</td>
    <td><a href="https://leetcode.com/problems/binary-tree-right-side-view/description/"
           target="_blank" class="text-link">Binary Tree Right Side View</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>BFS + preorder</td>
</tr>

<tr>
    <td>BST</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>98</td>
    <td><a href="https://leetcode.com/problems/validate-binary-search-tree/description/"
           target="_blank" class="text-link">Validate Binary Search Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>preorder</td>
</tr>
<tr>
    <td>235</td>
    <td><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/"
           target="_blank" class="text-link">Lowest Common Ancestor of a Binary Search Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>preorder</td>
</tr>
<tr>
    <td>236</td>
    <td><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/"
           target="_blank" class="text-link">Lowest Common Ancestor of a Binary Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>postorder</td>
</tr>
<tr>
    <td>108</td>
    <td><a href="https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/"
           target="_blank" class="text-link">Convert Sorted Array to Binary Search Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>binary search</td>
</tr>
<tr>
    <td>109</td>
    <td><a href="https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/"
           target="_blank" class="text-link"> Convert Sorted List to Binary Search Tree
    </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>binary search</td>
</tr>
<tr>
    <td>173</td>
    <td><a href="https://leetcode.com/problems/binary-search-tree-iterator/description/"
           target="_blank" class="text-link">Binary Search Tree Iterator</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>inorder</td>
</tr>
<tr>
    <td>230</td>
    <td><a href="https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/"
           target="_blank" class="text-link">Kth Smallest Element in a BST</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>inorder</td>
</tr>
<tr>
    <td>297</td>
    <td><a href="https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/"
           target="_blank" class="text-link">Serialize and Deserialize Binary Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>BFS</td>
</tr>
<tr>
    <td>285</td>
    <td><a href="https://leetcode.com/problems/inorder-successor-in-bst/description/"
           target="_blank" class="text-link">Inorder Successor in BST</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>inorder</td>
</tr>
<tr>
    <td>270</td>
    <td><a href="https://leetcode.com/problems/closest-binary-search-tree-value/description/"
           target="_blank" class="text-link">Closest Binary Search Tree Value</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>preorder</td>
</tr>
<tr>
    <td>272</td>
    <td><a href="https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/"
           target="_blank" class="text-link">Closest Binary Search Tree Value II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>inorder</td>
</tr>
<tr>
    <td>99</td>
    <td><a href="https://leetcode.com/problems/recover-binary-search-tree/"
           target="_blank" class="text-link">Recover Binary Search Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>inorder</td>
</tr>

<tr>
    <td>重要程度</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>156</td>
    <td><a href="https://leetcode.com/problems/binary-tree-upside-down/description/"
           target="_blank" class="text-link"> Binary Tree Upside Down</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>114</td>
    <td><a href="https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/"
           target="_blank" class="text-link">Flatten Binary Tree to Linked List</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>255</td>
    <td><a href="https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/"
           target="_blank" class="text-link">Verify Preorder Sequence in Binary Search Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>333</td>
    <td><a href="https://leetcode.com/problems/largest-bst-subtree/description/"
           target="_blank" class="text-link">Largest BST Subtree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>222</td>
    <td><a href="https://leetcode.com/problems/count-complete-tree-nodes/description/"
           target="_blank" class="text-link"> Count Complete Tree Nodes</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>105</td>
    <td><a href="https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/"
           target="_blank" class="text-link">Construct Binary Tree from Preorder and Inorder Traversal</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>106</td>
    <td><a href="https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/"
           target="_blank" class="text-link">Construct Binary Tree from Inorder and Postorder Traversal</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>116</td>
    <td><a href="https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/"
           target="_blank" class="text-link">Populating Next Right Pointers in Each Node</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>重要</td>
</tr>
<tr>
    <td>117</td>
    <td><a href="https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/"
           target="_blank" class="text-link"> Populating Next Right Pointers in Each Node II
    </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>重要</td>
</tr>
<tr>
    <td>314</td>
    <td><a href="https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/"
           target="_blank" class="text-link">Binary Tree Vertical Order Traversal</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>重要</td>
</tr>
<tr>
    <td>96</td>
    <td><a href="https://leetcode.com/problems/unique-binary-search-trees/description/"
           target="_blank" class="text-link">Unique Binary Search Trees</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>重要</td>
</tr>
<tr>
    <td>95</td>
    <td><a href="https://leetcode.com/problems/unique-binary-search-trees-ii/description/"
           target="_blank" class="text-link">Unique Binary Search Trees II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>331</td>
    <td><a href="https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/"
           target="_blank" class="text-link">Verify Preorder Serialization of a Binary Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--Backtracking-->
<div class="tab-pane fade" id="nav-Backtracking" role="tabpanel" aria-labelledby="nav-Backtracking">
    <div class="col-panel">
        <div class="col-header">Backtracking</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                    <td>说明</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>78</td>
    <td><a href="https://leetcode.com/problems/subsets/description/"
           target="_blank" class="text-link">Subsets</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>90</td>
    <td><a href="https://leetcode.com/problems/subsets-ii/description/"
           target="_blank" class="text-link">Subsets II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>77</td>
    <td><a href="https://leetcode.com/problems/combinations/description/"
           target="_blank" class="text-link">Combinations</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>39</td>
    <td><a href="https://leetcode.com/problems/combination-sum/description/"
           target="_blank" class="text-link">Combination Sum </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>40</td>
    <td><a href="https://leetcode.com/problems/combination-sum-ii/description/"
           target="_blank" class="text-link">Combination Sum II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>216</td>
    <td><a href="https://leetcode.com/problems/combination-sum-iii/description/"
           target="_blank" class="text-link">Combination Sum III</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>377</td>
    <td><a href="https://leetcode.com/problems/combination-sum-iv/description/"
           target="_blank" class="text-link"> Combination Sum IV</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>Dynamic Programming</td>
</tr>
<tr>
    <td>254</td>
    <td><a href="https://leetcode.com/problems/factor-combinations/description/"
           target="_blank" class="text-link">Factor Combinations</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>46</td>
    <td><a href="https://leetcode.com/problems/permutations/description/"
           target="_blank" class="text-link">Permutations</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>47</td>
    <td><a href="https://leetcode.com/problems/permutations-ii/description/"
           target="_blank" class="text-link">Permutations II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>31</td>
    <td><a href="https://leetcode.com/problems/next-permutation/description/"
           target="_blank" class="text-link">Next Permutation</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>String</td>
</tr>
<tr>
    <td>60</td>
    <td><a href="https://leetcode.com/problems/permutation-sequence/description/"
           target="_blank" class="text-link">Permutation Sequence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>String</td>
</tr>
<tr>
    <td>291</td>
    <td><a href="https://leetcode.com/problems/word-pattern-ii/description/"
           target="_blank" class="text-link">Word Pattern II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>17</td>
    <td><a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/"
           target="_blank" class="text-link">Letter Combinations of a Phone Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>320</td>
    <td><a href="https://leetcode.com/problems/generalized-abbreviation/description/"
           target="_blank" class="text-link">Generalized Abbreviation</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>93</td>
    <td><a href="https://leetcode.com/problems/restore-ip-addresses/description/"
           target="_blank" class="text-link">Restore IP Addresses</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>282</td>
    <td><a href="https://leetcode.com/problems/expression-add-operators/description/"
           target="_blank" class="text-link">Expression Add Operators</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>140</td>
    <td><a href="https://leetcode.com/problems/word-break-ii/description/"
           target="_blank" class="text-link">Word Break II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>351</td>
    <td><a href="https://leetcode.com/problems/android-unlock-patterns/description/"
           target="_blank" class="text-link">Android Unlock Patterns</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--Dynamic Programming-->
<div class="tab-pane fade" id="nav-DynamicProgramming" role="tabpanel" aria-labelledby="nav-DynamicProgramming">
    <div class="col-panel">
        <div class="col-header">Dynamic Programming</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                    <td>说明</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>一维</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>70</td>
    <td><a href="https://leetcode.com/problems/climbing-stairs/description/"
           target="_blank" class="text-link">Climbing Stairs</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>62</td>
    <td><a href="https://leetcode.com/problems/unique-paths/description/"
           target="_blank" class="text-link">Unique Paths</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>63</td>
    <td><a href="https://leetcode.com/problems/unique-paths-ii/description/"
           target="_blank" class="text-link">Unique Paths II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>120</td>
    <td><a href="https://leetcode.com/problems/triangle/description/"
           target="_blank" class="text-link">Triangle</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>279</td>
    <td><a href="https://leetcode.com/problems/perfect-squares/description/"
           target="_blank" class="text-link">Perfect Squares</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>139</td>
    <td><a href="https://leetcode.com/problems/word-break/"
           target="_blank" class="text-link">Word Break</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>375</td>
    <td><a href="https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/"
           target="_blank" class="text-link"> Guess Number Higher or Lower II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>312</td>
    <td><a href="https://leetcode.com/problems/burst-balloons/description/"
           target="_blank" class="text-link">Burst Balloons</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>322</td>
    <td><a href="https://leetcode.com/problems/coin-change/description/"
           target="_blank" class="text-link">Coin Change</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>二维</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>256</td>
    <td><a href="https://leetcode.com/problems/paint-house/description/"
           target="_blank" class="text-link">Paint House</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>265</td>
    <td><a href="https://leetcode.com/problems/paint-house-ii/description/"
           target="_blank" class="text-link">Paint House II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>64</td>
    <td><a href="https://leetcode.com/problems/minimum-path-sum/description/"
           target="_blank" class="text-link"> Minimum Path Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>72</td>
    <td><a href="https://leetcode.com/problems/edit-distance/description/"
           target="_blank" class="text-link">Edit Distance</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>97</td>
    <td><a href="https://leetcode.com/problems/interleaving-string/description/"
           target="_blank" class="text-link">Interleaving String</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>174</td>
    <td><a href="https://leetcode.com/problems/dungeon-game/description/"
           target="_blank" class="text-link">Dungeon Game</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>221</td>
    <td><a href="https://leetcode.com/problems/maximal-square/description/"
           target="_blank" class="text-link">Maximal Square</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>85</td>
    <td><a href="https://leetcode.com/problems/maximal-rectangle/description/"
           target="_blank" class="text-link">Maximal Rectangle</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>363</td>
    <td><a href="https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/"
           target="_blank" class="text-link">Max Sum of Rectangle No Larger Than K</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>TreeSet</td>
</tr>

<tr>
    <td>化简</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>198</td>
    <td><a href="https://leetcode.com/problems/house-robber/"
           target="_blank" class="text-link">House Robber</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>213</td>
    <td><a href="" target="_blank" class="text-link">House Robber II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>276</td>
    <td><a href="https://leetcode.com/problems/paint-fence/description/"
           target="_blank" class="text-link">Paint Fence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>91</td>
    <td><a href="https://leetcode.com/problems/decode-ways/description/"
           target="_blank" class="text-link">Decode Ways</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>10</td>
    <td><a href="https://leetcode.com/problems/regular-expression-matching/description/"
           target="_blank" class="text-link">Regular Expression Matching</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>44</td>
    <td><a href="https://leetcode.com/problems/wildcard-matching/description/"
           target="_blank" class="text-link">Wildcard Matching</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--LinkedList.ftl-->
<div class="tab-pane fade" id="nav-LinkedList" role="tabpanel" aria-labelledby="nav-LinkedList">
    <div class="col-panel">
        <div class="col-header">LinkedList</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>基础</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>206</td>
    <td><a href="https://leetcode.com/problems/reverse-linked-list/description/"
           target="_blank" class="text-link">Reverse Linked List</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>141</td>
    <td><a href="https://leetcode.com/problems/linked-list-cycle/description/"
           target="_blank" class="text-link">Linked List Cycle</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>24</td>
    <td><a href="https://leetcode.com/problems/swap-nodes-in-pairs/description/"
           target="_blank" class="text-link">Swap Nodes in Pairs</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>328</td>
    <td><a href="https://leetcode.com/problems/odd-even-linked-list/description/"
           target="_blank" class="text-link">Odd Even Linked List</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>92</td>
    <td><a href="https://leetcode.com/problems/reverse-linked-list-ii/description/"
           target="_blank" class="text-link">Reverse Linked List II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>237</td>
    <td><a href="https://leetcode.com/problems/delete-node-in-a-linked-list/description/"
           target="_blank" class="text-link">Delete Node in a Linked List</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>19</td>
    <td><a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/"
           target="_blank" class="text-link">Remove Nth Node From End of List</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>83</td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/"
           target="_blank" class="text-link">Remove Duplicates from Sorted List</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>203</td>
    <td><a href="https://leetcode.com/problems/remove-linked-list-elements/description/"
           target="_blank" class="text-link">Remove Linked List Elements</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>82</td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/"
           target="_blank" class="text-link">Remove Duplicates from Sorted List II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>369</td>
    <td><a href="https://leetcode.com/problems/plus-one-linked-list/description/"
           target="_blank" class="text-link">Plus One Linked List</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>2</td>
    <td><a href="https://leetcode.com/problems/add-two-numbers/description/"
           target="_blank" class="text-link">Add Two Numbers</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>160</td>
    <td><a href="https://leetcode.com/problems/intersection-of-two-linked-lists/description/"
           target="_blank" class="text-link">Intersection of Two Linked Lists</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>21</td>
    <td><a href="https://leetcode.com/problems/merge-two-sorted-lists/description/"
           target="_blank" class="text-link">Merge Two Sorted Lists</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>提高</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>234</td>
    <td><a href="https://leetcode.com/problems/palindrome-linked-list/description/"
           target="_blank" class="text-link"> Palindrome Linked List</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>143</td>
    <td><a href="https://leetcode.com/problems/reorder-list/description/"
           target="_blank" class="text-link">Reorder List</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>142</td>
    <td><a href="https://leetcode.com/problems/linked-list-cycle-ii/description/"
           target="_blank" class="text-link">Linked List Cycle II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>148</td>
    <td><a href="https://leetcode.com/problems/sort-list/description/"
           target="_blank" class="text-link">Sort List</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>25</td>
    <td><a href="https://leetcode.com/problems/reverse-nodes-in-k-group/description/"
           target="_blank" class="text-link">Reverse Nodes in k-Group</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>61</td>
    <td><a href="https://leetcode.com/problems/rotate-list/description/"
           target="_blank" class="text-link">Rotate List</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>86</td>
    <td><a href="https://leetcode.com/problems/partition-list/description/"
           target="_blank" class="text-link">Partition List</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>23</td>
    <td><a href="https://leetcode.com/problems/merge-k-sorted-lists/description/"
           target="_blank" class="text-link">Merge k Sorted Lists</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>147</td>
    <td><a href="https://leetcode.com/problems/insertion-sort-list/description/"
           target="_blank" class="text-link">Insertion Sort List</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--Binary Search-->
<div class="tab-pane fade" id="nav-BinarySearch" role="tabpanel" aria-labelledby="nav-BinarySearch">
    <div class="col-panel">
        <div class="col-header">Binary Search</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>278</td>
    <td><a href="https://leetcode.com/problems/first-bad-version/description/"
           target="_blank" class="text-link"> First Bad Version</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>35</td>
    <td><a href="https://leetcode.com/problems/search-insert-position/description/"
           target="_blank" class="text-link">Search Insert Position</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>33</td>
    <td><a href="https://leetcode.com/problems/search-in-rotated-sorted-array/description/"
           target="_blank" class="text-link">Search in Rotated Sorted Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>81</td>
    <td><a href="https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/"
           target="_blank" class="text-link">Search in Rotated Sorted Array II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>153</td>
    <td><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/"
           target="_blank" class="text-link">Find Minimum in Rotated Sorted Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>154</td>
    <td><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/"
           target="_blank" class="text-link">Find Minimum in Rotated Sorted Array II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>162</td>
    <td><a href="https://leetcode.com/problems/find-peak-element/description/"
           target="_blank" class="text-link">Find Peak Element </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>374</td>
    <td><a href="https://leetcode.com/problems/guess-number-higher-or-lower/"
           target="_blank" class="text-link">Guess Number Higher or Lower</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>34</td>
    <td><a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/"
           target="_blank" class="text-link"> Find First and Last Position of Element in Sorted Array
    </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>349</td>
    <td><a href="https://leetcode.com/problems/intersection-of-two-arrays/description/"
           target="_blank" class="text-link">Intersection of Two Arrays</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>350</td>
    <td><a href="https://leetcode.com/problems/intersection-of-two-arrays-ii/description/"
           target="_blank" class="text-link">Intersection of Two Arrays II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>315</td>
    <td><a href="https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/"
           target="_blank" class="text-link">Count of Smaller Numbers After Self</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>300</td>
    <td><a href="https://leetcode.com/problems/longest-increasing-subsequence/description/"
           target="_blank" class="text-link">Longest Increasing Subsequence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>354</td>
    <td><a href="https://leetcode.com/problems/russian-doll-envelopes/description/"
           target="_blank" class="text-link">Russian Doll Envelopes</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--Matrix-->
<div class="tab-pane fade" id="nav-Matrix" role="tabpanel" aria-labelledby="nav-Matrix">
    <div class="col-panel">
        <div class="col-header">Matrix</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>48</td>
    <td><a href="https://leetcode.com/problems/rotate-image/description/"
           target="_blank" class="text-link">Rotate Image</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>54</td>
    <td><a href="https://leetcode.com/problems/spiral-matrix/description/"
           target="_blank" class="text-link">Spiral Matrix</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>59</td>
    <td><a href="https://leetcode.com/problems/spiral-matrix-ii/description/"
           target="_blank" class="text-link">Spiral Matrix II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>73</td>
    <td><a href="https://leetcode.com/problems/set-matrix-zeroes/description/"
           target="_blank" class="text-link"> Set Matrix Zeroes</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>311</td>
    <td><a href="https://leetcode.com/problems/sparse-matrix-multiplication/description/"
           target="_blank" class="text-link">Sparse Matrix Multiplication</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>329</td>
    <td><a href="https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/"
           target="_blank" class="text-link">Longest Increasing Path in a Matrix</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>378</td>
    <td><a href="https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/"
           target="_blank" class="text-link">Kth Smallest Element in a Sorted Matrix</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>74</td>
    <td><a href="https://leetcode.com/problems/search-a-2d-matrix/description/"
           target="_blank" class="text-link">Search a 2D Matrix</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>240</td>
    <td><a href="https://leetcode.com/problems/search-a-2d-matrix-ii/description/"
           target="_blank" class="text-link">Search a 2D Matrix II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>370</td>
    <td><a href="https://leetcode.com/problems/range-addition/description/" 
           target="_blank" class="text-link">Range Addition</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>79</td>
    <td><a href="https://leetcode.com/problems/word-search/description/"
           target="_blank" class="text-link">Word Search</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>296</td>
    <td><a href="https://leetcode.com/problems/best-meeting-point/description/"
           target="_blank" class="text-link">Best Meeting Point</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>361</td>
    <td><a href="https://leetcode.com/problems/bomb-enemy/description/"
           target="_blank" class="text-link">Bomb Enemy</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>317</td>
    <td><a href="https://leetcode.com/problems/shortest-distance-from-all-buildings/description/"
           target="_blank" class="text-link">Shortest Distance from All Buildings</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>302</td>
    <td><a href="https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/description/"
           target="_blank" class="text-link">Smallest Rectangle Enclosing Black Pixels</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>36</td>
    <td><a href="https://leetcode.com/problems/valid-sudoku/description/"
           target="_blank" class="text-link">Valid Sudoku</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>37</td>
    <td><a href="https://leetcode.com/problems/sudoku-solver/description/"
           target="_blank" class="text-link">Sudoku Solver</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--DFS & BFS-->
<div class="tab-pane fade" id="nav-DFSBFS" role="tabpanel" aria-labelledby="nav-DFSBFS">
    <div class="col-panel">
        <div class="col-header">DFS & BFS</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>200</td>
    <td><a href="https://leetcode.com/problems/number-of-islands/"
           target="_blank" class="text-link">Number of Islands</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>286</td>
    <td><a href="https://leetcode.com/problems/walls-and-gates/description/"
           target="_blank" class="text-link">Walls and Gates</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>130</td>
    <td><a href="https://leetcode.com/problems/surrounded-regions/description/"
           target="_blank" class="text-link">Surrounded Regions</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>339</td>
    <td><a href="https://leetcode.com/problems/nested-list-weight-sum/description/"
           target="_blank" class="text-link">Nested List Weight Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>364</td>
    <td><a href="https://leetcode.com/problems/nested-list-weight-sum-ii/description/"
           target="_blank" class="text-link"> Nested List Weight Sum II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>127</td>
    <td><a href="https://leetcode.com/problems/word-ladder/description/"
           target="_blank" class="text-link"> Word Ladder</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>51</td>
    <td><a href="https://leetcode.com/problems/n-queens/"
           target="_blank" class="text-link">N-Queens</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>52</td>
    <td><a href="https://leetcode.com/problems/n-queens-ii/description/"
           target="_blank" class="text-link">N-Queens II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>126</td>
    <td><a href="https://leetcode.com/problems/word-ladder-ii/description/"
           target="_blank" class="text-link"> Word Ladder II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--Stack & PriorityQueue-->
<div class="tab-pane fade" id="nav-StackPriorityQueue" role="tabpanel" aria-labelledby="nav-StackPriorityQueue">
    <div class="col-panel">
        <div class="col-header">Stack & PriorityQueue</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                    <td>说明</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>Stack</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>155</td>
    <td><a href="https://leetcode.com/problems/min-stack/description/"
           target="_blank" class="text-link">Min Stack</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>232</td>
    <td><a href="https://leetcode.com/problems/implement-queue-using-stacks/description/"
           target="_blank" class="text-link">Implement Queue using Stacks</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>225</td>
    <td><a href="https://leetcode.com/problems/implement-stack-using-queues/description/"
           target="_blank" class="text-link">Implement Stack using Queues</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>150</td>
    <td><a href="https://leetcode.com/problems/evaluate-reverse-polish-notation/description/"
           target="_blank" class="text-link">Evaluate Reverse Polish Notation</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>71</td>
    <td><a href="https://leetcode.com/problems/simplify-path/description/"
           target="_blank" class="text-link">Simplify Path</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>388</td>
    <td><a href="https://leetcode.com/problems/longest-absolute-file-path/description/"
           target="_blank" class="text-link">Longest Absolute File Path</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>394</td>
    <td><a href="https://leetcode.com/problems/decode-string/"
           target="_blank" class="text-link">Decode String</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>224</td>
    <td><a href="https://leetcode.com/problems/basic-calculator/description/"
           target="_blank" class="text-link">Basic Calculator</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>227</td>
    <td><a href="https://leetcode.com/problems/basic-calculator-ii/description/"
           target="_blank" class="text-link">Basic Calculator II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>385</td>
    <td><a href="https://leetcode.com/problems/mini-parser/description/"
           target="_blank" class="text-link">Mini Parser</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>84</td>
    <td><a href="https://leetcode.com/problems/largest-rectangle-in-histogram/description/"
           target="_blank" class="text-link">Largest Rectangle in Histogram</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>PriorityQueue</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>215</td>
    <td><a href="https://leetcode.com/problems/kth-largest-element-in-an-array/description/"
           target="_blank" class="text-link">Kth Largest Element in an Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>347</td>
    <td><a href="https://leetcode.com/problems/top-k-frequent-elements/description/"
           target="_blank" class="text-link">Top K Frequent Elements</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>313</td>
    <td><a href="https://leetcode.com/problems/super-ugly-number/description/"
           target="_blank" class="text-link">Super Ugly Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>373</td>
    <td><a href="https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/"
           target="_blank" class="text-link">Find K Pairs with Smallest Sums</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>218</td>
    <td><a href="https://leetcode.com/problems/the-skyline-problem/description/"
           target="_blank" class="text-link"> The Skyline Problem</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>332</td>
    <td><a href="https://leetcode.com/problems/reconstruct-itinerary/description/"
           target="_blank" class="text-link">Reconstruct Itinerary</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>341</td>
    <td><a href="https://leetcode.com/problems/flatten-nested-list-iterator/"
           target="_blank" class="text-link">Flatten Nested List Iterator</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--Bit Manipulation-->
<div class="tab-pane fade" id="nav-BitManipulation" role="tabpanel" aria-labelledby="nav-BitManipulation">
    <div class="col-panel">
        <div class="col-header">Bit Manipulation</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>389</td>
    <td><a href="https://leetcode.com/problems/find-the-difference/description/"
           target="_blank" class="text-link">Find the Difference</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>136</td>
    <td><a href="https://leetcode.com/problems/single-number/description/"
           target="_blank" class="text-link">Single Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>318</td>
    <td><a href="https://leetcode.com/problems/maximum-product-of-word-lengths/description/"
           target="_blank" class="text-link"> Maximum Product of Word Lengths</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>很少考</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>393</td>
    <td><a href="https://leetcode.com/problems/utf-8-validation/description/"
           target="_blank" class="text-link"> UTF-8 Validation</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>201</td>
    <td><a href="https://leetcode.com/problems/bitwise-and-of-numbers-range/description/"
           target="_blank" class="text-link">Bitwise AND of Numbers Range</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>371</td>
    <td><a href="https://leetcode.com/problems/sum-of-two-integers/description/"
           target="_blank" class="text-link">Sum of Two Integers
        emove Element</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>338</td>
    <td><a href="https://leetcode.com/problems/counting-bits/description/"
           target="_blank" class="text-link">Counting Bits</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>89</td>
    <td><a href="https://leetcode.com/problems/gray-code/description/"
           target="_blank" class="text-link">Gray Code</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>268</td>
    <td><a href="https://leetcode.com/problems/missing-number/description/"
           target="_blank" class="text-link">Missing Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>191</td>
    <td><a href="https://leetcode.com/problems/number-of-1-bits/description/"
           target="_blank" class="text-link">Number of 1 Bits</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>190</td>
    <td><a href="https://leetcode.com/problems/reverse-bits/description/"
           target="_blank" class="text-link"> Reverse Bits</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>137</td>
    <td><a href="https://leetcode.com/problems/single-number-ii/description/"
           target="_blank" class="text-link">Single Number II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>260</td>
    <td><a href="https://leetcode.com/problems/single-number-iii/description/"
           target="_blank" class="text-link"> Single Number III
    </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--Topological Sort-->
<div class="tab-pane fade" id="nav-TopologicalSort" role="tabpanel" aria-labelledby="nav-TopologicalSort">
    <div class="col-panel">
        <div class="col-header">Topological Sort</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>207</td>
    <td><a href="https://leetcode.com/problems/course-schedule/description/"
           target="_blank" class="text-link">Course Schedule</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>210</td>
    <td><a href="https://leetcode.com/problems/course-schedule-ii/description/"
           target="_blank" class="text-link">Course Schedule II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>269</td>
    <td><a href="https://leetcode.com/problems/alien-dictionary/description/"
           target="_blank" class="text-link">Alien Dictionary</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--Random-->
<div class="tab-pane fade" id="nav-Random" role="tabpanel" aria-labelledby="nav-Random">
    <div class="col-panel">
        <div class="col-header">Random</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>384</td>
    <td><a href="https://leetcode.com/problems/shuffle-an-array/"
           target="_blank" class="text-link">Shuffle an Array</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>398</td>
    <td><a href="https://leetcode.com/problems/random-pick-index/"
           target="_blank" class="text-link">Random Pick Index</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>382</td>
    <td><a href="https://leetcode.com/problems/linked-list-random-node/"
           target="_blank" class="text-link">Linked List Random Node</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>380</td>
    <td><a href="https://leetcode.com/problems/insert-delete-getrandom-o1/"
           target="_blank" class="text-link">Insert Delete GetRandom O(1)</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>381</td>
    <td><a href="https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/"
           target="_blank" class="text-link">Insert Delete GetRandom O(1) - Duplicates allowed</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>138</td>
    <td><a href="https://leetcode.com/problems/copy-list-with-random-pointer/"
           target="_blank" class="text-link">Copy List with Random Pointer</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--Graph-->
<div class="tab-pane fade" id="nav-Graph" role="tabpanel" aria-labelledby="nav-Graph">
    <div class="col-panel">
        <div class="col-header">Graph</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                    <td>说明</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>基础</td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>133</td>
    <td><a href="https://leetcode.com/problems/clone-graph/description/"
           target="_blank" class="text-link">Clone Graph</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>399</td>
    <td><a href="https://leetcode.com/problems/evaluate-division/description/"
           target="_blank" class="text-link">Evaluate Division</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>310</td>
    <td><a href="https://leetcode.com/problems/minimum-height-trees/description/"
           target="_blank" class="text-link">Minimum Height Trees</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>图形学</td>
    <td></td>
    <td></td>
    <td></td>
</tr>

<tr>
    <td>149</td>
    <td><a href="https://leetcode.com/problems/max-points-on-a-line/description/"
           target="_blank" class="text-link">Max Points on a Line</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>335</td>
    <td><a href="https://leetcode.com/problems/self-crossing/description/"
           target="_blank" class="text-link">Self Crossing</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>356</td>
    <td><a href="https://leetcode.com/problems/line-reflection/description/"
           target="_blank" class="text-link">Line Reflection</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>391</td>
    <td><a href="https://leetcode.com/problems/perfect-rectangle/description/" 
           target="_blank" class="text-link">Perfect Rectangle</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>
<tr>
    <td>223</td>
    <td><a href="https://leetcode.com/problems/rectangle-area/description/" 
           target="_blank" class="text-link">Rectangle Area</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>很少考</td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--Union Find-->
<div class="tab-pane fade" id="nav-UnionFind" role="tabpanel" aria-labelledby="nav-UnionFind">
    <div class="col-panel">
        <div class="col-header">Union Find</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>261</td>
    <td><a href="https://leetcode.com/problems/graph-valid-tree/description/"
           target="_blank" class="text-link">Graph Valid Tree</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>323</td>
    <td><a href="https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/"
           target="_blank" class="text-link">Number of Connected Components in an Undirected Graph</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>305</td>
    <td><a href="https://leetcode.com/problems/number-of-islands-ii/description/"
           target="_blank" class="text-link">Number of Islands II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div>
<!--Trie-->
<div class="tab-pane fade" id="nav-Trie" role="tabpanel" aria-labelledby="nav-Trie">
    <div class="col-panel">
        <div class="col-header">Trie</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>211</td>
    <td><a href="https://leetcode.com/problems/add-and-search-word-data-structure-design/description/"
           target="_blank" class="text-link">Add and Search Word - Data structure design
    </a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>208</td>
    <td><a href="https://leetcode.com/problems/implement-trie-prefix-tree/description/"
           target="_blank" class="text-link">Implement Trie (Prefix Tree)
    </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>212</td>
    <td><a href="https://leetcode.com/problems/word-search-ii/description/"
           target="_blank" class="text-link">Word Search II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<!--Design-->
<div class="tab-pane fade" id="nav-Design" role="tabpanel" aria-labelledby="nav-Design">
    <div class="col-panel">
        <div class="col-header">Design</div>
        <div class="col-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <td>题号</td>
                    <td>题目链接</td>
                    <td>讲解链接</td>
                    <td>说明</td>
                </tr>
                </thead>
                <tbody>
<tr>
    <td>359</td>
    <td><a href="https://leetcode.com/problems/logger-rate-limiter/description/"
           target="_blank" class="text-link">Logger Rate Limiter</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>346</td>
    <td><a href="https://leetcode.com/problems/moving-average-from-data-stream/description/"
           target="_blank" class="text-link">Moving Average from Data Stream</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>Sliding Window</td>
</tr>
<tr>
    <td>362</td>
    <td><a href="https://leetcode.com/problems/design-hit-counter/description/"
           target="_blank" class="text-link">Design Hit Counter</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>281</td>
    <td><a href="https://leetcode.com/problems/zigzag-iterator/description/"
           target="_blank" class="text-link">Zigzag Iterator</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>284</td>
    <td><a href="https://leetcode.com/problems/peeking-iterator/description/"
           target="_blank" class="text-link">Peeking Iterator</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>251</td>
    <td><a href="https://leetcode.com/problems/flatten-2d-vector/description/s"
           target="_blank" class="text-link">Flatten 2D Vector</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>288</td>
    <td><a href="https://leetcode.com/problems/unique-word-abbreviation/description/"
           target="_blank" class="text-link">Unique Word Abbreviation</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>170</td>
    <td><a href="https://leetcode.com/problems/two-sum-iii-data-structure-design/description/"
           target="_blank" class="text-link">Two Sum III - Data structure design</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>348</td>
    <td><a href="https://leetcode.com/problems/design-tic-tac-toe/description/"
           target="_blank" class="text-link">Design Tic-Tac-Toe</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>379</td>
    <td><a href="https://leetcode.com/problems/design-phone-directory/description/"
           target="_blank" class="text-link">Design Phone Directory</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>353</td>
    <td><a href="https://leetcode.com/problems/design-snake-game/description/"
           target="_blank" class="text-link">Design Snake Game</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>146</td>
    <td><a href="https://leetcode.com/problems/lru-cache/description/"
           target="_blank" class="text-link">LRU Cache</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>355</td>
    <td><a href="https://leetcode.com/problems/design-twitter/description/s"
           target="_blank" class="text-link">Design Twitter</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>303</td>
    <td><a href="https://leetcode.com/problems/range-sum-query-immutable/description/"
           target="_blank" class="text-link">Range Sum Query - Immutable</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>304</td>
    <td><a href="https://leetcode.com/problems/range-sum-query-2d-immutable/description/"
           target="_blank" class="text-link">Range Sum Query 2D - Immutable</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>307</td>
    <td><a href="https://leetcode.com/problems/range-sum-query-mutable/description/"
           target="_blank" class="text-link">Range Sum Query - Mutable</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>BIT & ST</td>
</tr>
<tr>
    <td>308</td>
    <td><a href="https://leetcode.com/problems/range-sum-query-2d-mutable/description/"
           target="_blank" class="text-link">Range Sum Query 2D - Mutable</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td>BIT & ST</td>
</tr>                </tbody>
            </table>
        </div>
    </div>
</div><!--刷题多少才算够-->
<div class="tab-pane fade" id="nav-question1" role="tabpanel" aria-labelledby="nav-question1">
    <div class="col-panel">
        <div class="col-header">分类顺序表400题，刷这些够吗，剩下的怎么办？</div>
        <div class="col-body">
            <div class="col-cell">
                <div class="cell-body">
                    <div class="cell-intro">
                        <p>如果能把Leetcode 前400题都刷透，再做做面经题，足以面试各大公司。</p>
                        <p>或者说，以算法题角度，横扫各大公司。</p>
                        <p>但在现实生活中，能把400题刷明白的，十中无一。</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!--我想提问题-->
<div class="tab-pane fade" id="nav-question2" role="tabpanel" aria-labelledby="nav-question2">
    <div class="col-panel">
        <div class="col-header">我想提问题</div>
        <div class="col-body">
            <div class="col-cell">
                <div class="cell-body">
                    <div class="cell-intro">
                        <p>有问题，可以在这个word里提问，近期我们会集中回答。</p>
                        <p><a href="https://docs.google.com/document/d/1Kp2OhWtqM3qZClV5sMMeR6SF4S2JxhDsDqxv2JZ6he0/edit" target="_blank">提问题链接（点我）</a></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>                        <!--Data Science 划分说明-->
                        <div class="tab-pane fade" id="nav-DShuafenshuoming" role="tabpanel" aria-labelledby="nav-DShuafenshuoming">
                            <div class="col-panel">
                                <div class="col-header">划分说明</div>
                                <div class="col-body">
                                    此表是针对 Data Science 这个职位，对Leetcode前400题进行精简，划分精简规则如下：
                                    </br>
                                    <ul class="kc-list list-unstyled" style="padding-top: 10px">
                                        <li class="dot">删除DS不常考，面试低频出现题目</li>
                                        <li class="dot">删除SDE考，过难题目</li>
                                        <li class="dot">删除高级数据结构算法，保留基础简单题目</li>
                                        <li class="dot">保留基础练手题目，提高代码能力</li>
                                    </ul>
                                    </br>
                                    <p>
                                        所有题目我们尽量保证客观公正，只是按大概率删除，目的是为了减轻DS的刷题负担。
                                    </p>
                                    <p>
                                        适用人群：Data Science 职位相关人员
                                    </p>
                                </div>
                            </div>
                        </div>
                        <!--划分说明-->
                        <div class="tab-pane fade" id="nav-huafenshuoming" role="tabpanel" aria-labelledby="nav-huafenshuoming">
                            <div class="col-panel">
                                <div class="col-header">划分说明</div>
                                <div class="col-body">
                                    这个重点题目是把Leetcode前400题进行精简，划分精简规则如下：
                                    </br>
                                    <ul class="kc-list list-unstyled" style="padding-top: 10px">
                                        <li class="dot">删除不常考，面试低频出现题目</li>
                                        <li class="dot">删除重复代码题目（例：链表反转206题，代码在234题出现过）</li>
                                        <li class="dot">删除过于简单题目（例：100题：Same Tree）</li>
                                        <li class="dot">删除题意不同，代码基本相同题目（例：136 & 389，保留一个）</li>
                                    </ul>
                                    </br>
                                    <p>
                                        所有题目尽量保证客观公正，只是按大概率删除不常考题目，很多题目面经出现过，
                                        但出现次数属于个位数或者只有一两家出现进行删除。所以如在面试中出现删除题目概不负责，这只是从概率上删除低频，简单题目。
                                        旨在减轻大家的刷题负担，从400题减少到250题。
                                    </p>
                                    <p>
                                        适用人群：有一定刷题基础，算法基础，二刷人群。
                                    </p>
                                    <strong>建议：400题全部刷完，再精刷这250题。</strong>
                                </div>
                            </div>
                        </div>
                        <!--重点题目-->
                        <div class="tab-pane fade" id="nav-zhongdiantimu" role="tabpanel" aria-labelledby="nav-zhongdiantimu">
                            <div class="col-panel">
                                <div class="col-header">Leetcode 前 400 重点 250 题</div>
                                <div class="col-body">
                                    <table class="table table-striped">
                                        <thead>
                                        <tr>
                                            <td>题号</td>
                                            <td>题目名称</td>
                                            <td>讲解链接</td>
                                            <td></td>
                                        </tr>
                                        </thead>
                                        <tbody>
<tr>
    <td>1</td>
    <td><a href="https://leetcode.com/problems/two-sum/description/"
           target="_blank" class="text-link">Two Sum</a></td>
            <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>3</td>
    <td><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/description/"
           target="_blank" class="text-link">Longest Substring Without Repeating Characters</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>4</td>
    <td><a href="https://leetcode.com/problems/median-of-two-sorted-arrays/description/"
           target="_blank" class="text-link">Median of Two Sorted Arrays</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>5</td>
    <td><a href="https://leetcode.com/problems/longest-palindromic-substring/description/"
           target="_blank" class="text-link">Longest Palindromic Substring
    </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>7</td>
    <td><a href="https://leetcode.com/problems/reverse-integer/description/"
           target="_blank" class="text-link">Reverse Integer</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>8</td>
    <td><a href="https://leetcode.com/problems/string-to-integer-atoi/description/"
           target="_blank" class="text-link">String to Integer (atoi)</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>10</td>
    <td><a href="https://leetcode.com/problems/regular-expression-matching/description/"
           target="_blank" class="text-link">Regular Expression Matching</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>11</td>
    <td><a href="https://leetcode.com/problems/container-with-most-water/description/"
           target="_blank" class="text-link">Container With Most Water</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>12</td>
    <td><a href="https://leetcode.com/problems/integer-to-roman/description/"
           target="_blank" class="text-link">Integer to Roman</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>13</td>
    <td><a href="https://leetcode.com/problems/roman-to-integer/description/"
           target="_blank" class="text-link">Roman to Integer</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>15</td>
    <td><a href="https://leetcode.com/problems/3sum/description/"
           target="_blank" class="text-link">3Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>17</td>
    <td><a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/"
           target="_blank" class="text-link">Letter Combinations of a Phone Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>18</td>
    <td><a href="https://leetcode.com/problems/4sum/description/"
           target="_blank" class="text-link">4Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>20</td>
    <td><a href="https://leetcode.com/problems/valid-parentheses/description/"
           target="_blank" class="text-link">Valid Parentheses</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>22</td>
    <td><a href="https://leetcode.com/problems/generate-parentheses/description/"
           target="_blank" class="text-link">Generate Parentheses</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>23</td>
    <td><a href="https://leetcode.com/problems/merge-k-sorted-lists/description/"
           target="_blank" class="text-link">Merge k Sorted Lists</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>26</td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/"
           target="_blank" class="text-link">Remove Duplicates from Sorted Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>27</td>
    <td><a href="https://leetcode.com/problems/remove-element/"
           target="_blank" class="text-link">Remove Element</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>

    <td></td>
</tr>
<tr>
    <td>28</td>
    <td><a href="https://leetcode.com/problems/implement-strstr/description/"
           target="_blank" class="text-link">Implement strStr()</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>29</td>
    <td><a href="https://leetcode.com/problems/divide-two-integers/description/"
           target="_blank" class="text-link">Divide Two Integers</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>31</td>
    <td><a href="https://leetcode.com/problems/next-permutation/description/"
           target="_blank" class="text-link">Next Permutation</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>32</td>
    <td><a href="https://leetcode.com/problems/longest-valid-parentheses/description/"
           target="_blank" class="text-link">Longest Valid Parentheses</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>33</td>
    <td><a href="https://leetcode.com/problems/search-in-rotated-sorted-array/description/"
           target="_blank" class="text-link">Search in Rotated Sorted Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>34</td>
    <td><a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/"
           target="_blank" class="text-link"> Find First and Last Position of Element in Sorted Array
    </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>35</td>
    <td><a href="https://leetcode.com/problems/search-insert-position/description/"
           target="_blank" class="text-link">Search Insert Position</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>36</td>
    <td><a href="https://leetcode.com/problems/valid-sudoku/description/"
           target="_blank" class="text-link">Valid Sudoku</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>37</td>
    <td><a href="https://leetcode.com/problems/sudoku-solver/description/"
           target="_blank" class="text-link">Sudoku Solver</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>38</td>
    <td><a href="https://leetcode.com/problems/count-and-say/description/"
           target="_blank" class="text-link">Count and Say</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>39</td>
    <td><a href="https://leetcode.com/problems/combination-sum/description/"
           target="_blank" class="text-link">Combination Sum </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>40</td>
    <td><a href="https://leetcode.com/problems/combination-sum-ii/description/"
           target="_blank" class="text-link">Combination Sum II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>41</td>
    <td><a href="https://leetcode.com/problems/first-missing-positive/description/"
           target="_blank" class="text-link">First Missing Positive</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>42</td>
    <td><a href="https://leetcode.com/problems/trapping-rain-water/description/"
           target="_blank" class="text-link">Trapping Rain Water</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>43</td>
    <td><a href="https://leetcode.com/problems/multiply-strings/description/"
           target="_blank" class="text-link">Multiply Strings</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>44</td>
    <td><a href="https://leetcode.com/problems/wildcard-matching/description/"
           target="_blank" class="text-link">Wildcard Matching</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>45</td>
    <td><a href="https://leetcode.com/problems/jump-game-ii/description/"
           target="_blank" class="text-link">Jump Game II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>46</td>
    <td><a href="https://leetcode.com/problems/permutations/description/"
           target="_blank" class="text-link">Permutations</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>47</td>
    <td><a href="https://leetcode.com/problems/permutations-ii/description/"
           target="_blank" class="text-link">Permutations II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>48</td>
    <td><a href="https://leetcode.com/problems/rotate-image/description/"
           target="_blank" class="text-link">Rotate Image</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>49</td>
    <td><a href="https://leetcode.com/problems/group-anagrams/description/"
           target="_blank" class="text-link">Group Anagrams</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>50</td>
    <td><a href="https://leetcode.com/problems/powx-n/description/" target="_blank"
           class="text-link">Pow(x, n)</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>51</td>
    <td><a href="https://leetcode.com/problems/n-queens/"
           target="_blank" class="text-link">N-Queens</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>52</td>
    <td><a href="https://leetcode.com/problems/n-queens-ii/description/"
           target="_blank" class="text-link">N-Queens II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>53</td>
    <td><a href="https://leetcode.com/problems/maximum-subarray/description/"
           target="_blank" class="text-link">Maximum Subarray</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>54</td>
    <td><a href="https://leetcode.com/problems/spiral-matrix/description/"
           target="_blank" class="text-link">Spiral Matrix</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>55</td>
    <td><a href="https://leetcode.com/problems/jump-game/description/"
           target="_blank" class="text-link">Jump Game</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>56</td>
    <td><a href="https://leetcode.com/problems/merge-intervals/description/"
           target="_blank" class="text-link">Merge Intervals</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>57</td>
    <td><a href="https://leetcode.com/problems/insert-interval/description/"
           target="_blank" class="text-link">Insert Interval</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>59</td>
    <td><a href="https://leetcode.com/problems/spiral-matrix-ii/description/"
           target="_blank" class="text-link">Spiral Matrix II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>60</td>
    <td><a href="https://leetcode.com/problems/permutation-sequence/description/"
           target="_blank" class="text-link">Permutation Sequence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>62</td>
    <td><a href="https://leetcode.com/problems/unique-paths/description/"
           target="_blank" class="text-link">Unique Paths</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>64</td>
    <td><a href="https://leetcode.com/problems/minimum-path-sum/description/"
           target="_blank" class="text-link"> Minimum Path Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>65</td>
    <td><a href="https://leetcode.com/problems/valid-number/description/"
           target="_blank" class="text-link">Valid Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>66</td>
    <td><a href="https://leetcode.com/problems/plus-one/description/"
           target="_blank" class="text-link">Plus One</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>67</td>
    <td><a href="https://leetcode.com/problems/add-binary/description/"
           target="_blank" class="text-link">Add Binary</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>68</td>
    <td><a href="https://leetcode.com/problems/text-justification/description/"
           target="_blank" class="text-link">Text Justification</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>69</td>
    <td><a href="https://leetcode.com/problems/sqrtx/description/"
           target="_blank" class="text-link">Sqrt(x)</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>70</td>
    <td><a href="https://leetcode.com/problems/climbing-stairs/description/"
           target="_blank" class="text-link">Climbing Stairs</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>71</td>
    <td><a href="https://leetcode.com/problems/simplify-path/description/"
           target="_blank" class="text-link">Simplify Path</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>72</td>
    <td><a href="https://leetcode.com/problems/edit-distance/description/"
           target="_blank" class="text-link">Edit Distance</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>74</td>
    <td><a href="https://leetcode.com/problems/search-a-2d-matrix/description/"
           target="_blank" class="text-link">Search a 2D Matrix</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>75</td>
    <td><a href="https://leetcode.com/problems/sort-colors/description/"
           target="_blank" class="text-link">Sort Colors</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>76</td>
    <td><a href="https://leetcode.com/problems/minimum-window-substring/description/"
           target="_blank" class="text-link">Minimum Window Substring</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>77</td>
    <td><a href="https://leetcode.com/problems/combinations/description/"
           target="_blank" class="text-link">Combinations</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>78</td>
    <td><a href="https://leetcode.com/problems/subsets/description/"
           target="_blank" class="text-link">Subsets</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>79</td>
    <td><a href="https://leetcode.com/problems/word-search/description/"
           target="_blank" class="text-link">Word Search</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>80</td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/"
           target="_blank" class="text-link">Remove Duplicates from Sorted Array II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>81</td>
    <td><a href="https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/"
           target="_blank" class="text-link">Search in Rotated Sorted Array II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>82</td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/"
           target="_blank" class="text-link">Remove Duplicates from Sorted List II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>84</td>
    <td><a href="https://leetcode.com/problems/largest-rectangle-in-histogram/description/"
           target="_blank" class="text-link">Largest Rectangle in Histogram</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>85</td>
    <td><a href="https://leetcode.com/problems/maximal-rectangle/description/"
           target="_blank" class="text-link">Maximal Rectangle</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>88</td>
    <td><a href="https://leetcode.com/problems/merge-sorted-array/description/"
           target="_blank" class="text-link">Merge Sorted Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>90</td>
    <td><a href="https://leetcode.com/problems/subsets-ii/description/"
           target="_blank" class="text-link">Subsets II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>91</td>
    <td><a href="https://leetcode.com/problems/decode-ways/description/"
           target="_blank" class="text-link">Decode Ways</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>96</td>
    <td><a href="https://leetcode.com/problems/unique-binary-search-trees/description/"
           target="_blank" class="text-link">Unique Binary Search Trees</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>98</td>
    <td><a href="https://leetcode.com/problems/validate-binary-search-tree/description/"
           target="_blank" class="text-link">Validate Binary Search Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>101</td>
    <td><a href="https://leetcode.com/problems/symmetric-tree/description/"
           target="_blank" class="text-link">Symmetric Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>104</td>
    <td><a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/description/"
           target="_blank" class="text-link">Maximum Depth of Binary Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>108</td>
    <td><a href="https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/"
           target="_blank" class="text-link">Convert Sorted Array to Binary Search Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>110</td>
    <td><a href="https://leetcode.com/problems/balanced-binary-tree/description/"
           target="_blank" class="text-link">Balanced Binary Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>111</td>
    <td><a href="https://leetcode.com/problems/minimum-depth-of-binary-tree/description/"
           target="_blank" class="text-link">Minimum Depth of Binary Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>112</td>
    <td><a href="https://leetcode.com/problems/path-sum/description/" target="_blank" class="text-link">Path Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>113</td>
    <td><a href="https://leetcode.com/problems/path-sum-ii/description/"
           target="_blank" class="text-link">Path Sum II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>115</td>
    <td><a href="https://leetcode.com/problems/distinct-subsequences/description/"
           target="_blank" class="text-link">Distinct Subsequences</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>116</td>
    <td><a href="https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/"
           target="_blank" class="text-link">Populating Next Right Pointers in Each Node</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>117</td>
    <td><a href="https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/"
           target="_blank" class="text-link"> Populating Next Right Pointers in Each Node II
    </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>121</td>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/"
           target="_blank" class="text-link">Best Time to Buy and Sell Stock</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>122</td>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/"
           target="_blank" class="text-link"> Best Time to Buy and Sell Stock II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>123</td>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/"
           target="_blank" class="text-link">Best Time to Buy and Sell Stock III</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>124</td>
    <td><a href="https://leetcode.com/problems/binary-tree-maximum-path-sum/description/"
           target="_blank" class="text-link">Binary Tree Maximum Path Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>125</td>
    <td><a href="https://leetcode.com/problems/valid-palindrome/description/"
           target="_blank" class="text-link">Valid Palindrome</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>126</td>
    <td><a href="https://leetcode.com/problems/word-ladder-ii/description/"
           target="_blank" class="text-link"> Word Ladder II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>127</td>
    <td><a href="https://leetcode.com/problems/word-ladder/description/"
           target="_blank" class="text-link"> Word Ladder</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>128</td>
    <td><a href="https://leetcode.com/problems/longest-consecutive-sequence/description/"
           target="_blank" class="text-link">Longest Consecutive Sequence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>130</td>
    <td><a href="https://leetcode.com/problems/surrounded-regions/description/"
           target="_blank" class="text-link">Surrounded Regions</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>133</td>
    <td><a href="https://leetcode.com/problems/clone-graph/description/"
           target="_blank" class="text-link">Clone Graph</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>134</td>
    <td><a href="https://leetcode.com/problems/gas-station/description/"
           target="_blank" class="text-link">Gas Station</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>138</td>
    <td><a href="https://leetcode.com/problems/copy-list-with-random-pointer/"
           target="_blank" class="text-link">Copy List with Random Pointer</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>139</td>
    <td><a href="https://leetcode.com/problems/word-break/"
           target="_blank" class="text-link">Word Break</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>140</td>
    <td><a href="https://leetcode.com/problems/word-break-ii/description/"
           target="_blank" class="text-link">Word Break II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>142</td>
    <td><a href="https://leetcode.com/problems/linked-list-cycle-ii/description/"
           target="_blank" class="text-link">Linked List Cycle II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>146</td>
    <td><a href="https://leetcode.com/problems/lru-cache/description/"
           target="_blank" class="text-link">LRU Cache</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>149</td>
    <td><a href="https://leetcode.com/problems/max-points-on-a-line/description/"
           target="_blank" class="text-link">Max Points on a Line</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>150</td>
    <td><a href="https://leetcode.com/problems/evaluate-reverse-polish-notation/description/"
           target="_blank" class="text-link">Evaluate Reverse Polish Notation</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>152</td>
    <td><a href="https://leetcode.com/problems/maximum-product-subarray/description/"
           target="_blank" class="text-link">Maximum Product Subarray</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>153</td>
    <td><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/"
           target="_blank" class="text-link">Find Minimum in Rotated Sorted Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>154</td>
    <td><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/"
           target="_blank" class="text-link">Find Minimum in Rotated Sorted Array II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>155</td>
    <td><a href="https://leetcode.com/problems/min-stack/description/"
           target="_blank" class="text-link">Min Stack</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>157</td>
    <td><a href="https://leetcode.com/problems/read-n-characters-given-read4/description/"
           target="_blank" class="text-link">Read N Characters Given Read4</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>158</td>
    <td><a href="https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/description/"
           target="_blank" class="text-link">Read N Characters Given Read4 II - Call multiple times</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>161</td>
    <td><a href="https://leetcode.com/problems/one-edit-distance/"
           target="_blank" class="text-link">One Edit Distance</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>162</td>
    <td><a href="https://leetcode.com/problems/find-peak-element/description/"
           target="_blank" class="text-link">Find Peak Element </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>163</td>
    <td><a href="https://leetcode.com/problems/missing-ranges/description/"
           target="_blank" class="text-link">Missing Ranges</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>168</td>
    <td><a href="https://leetcode.com/problems/excel-sheet-column-title/description/"
           target="_blank" class="text-link">Excel Sheet Column Title</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>171</td>
    <td><a href="https://leetcode.com/problems/excel-sheet-column-number/description/"
           target="_blank" class="text-link">Excel Sheet Column Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>173</td>
    <td><a href="https://leetcode.com/problems/binary-search-tree-iterator/description/"
           target="_blank" class="text-link">Binary Search Tree Iterator</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>174</td>
    <td><a href="https://leetcode.com/problems/dungeon-game/description/"
           target="_blank" class="text-link">Dungeon Game</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>186</td>
    <td><a href="https://leetcode.com/problems/reverse-words-in-a-string-ii/description/"
           target="_blank" class="text-link">Reverse Words in a String II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>188</td>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/"
           target="_blank" class="text-link">Best Time to Buy and Sell Stock IV</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>189</td>
    <td><a href="https://leetcode.com/problems/rotate-array/description/"
           target="_blank" class="text-link">Rotate Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>191</td>
    <td><a href="https://leetcode.com/problems/number-of-1-bits/description/"
           target="_blank" class="text-link">Number of 1 Bits</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>198</td>
    <td><a href="https://leetcode.com/problems/house-robber/"
           target="_blank" class="text-link">House Robber</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>200</td>
    <td><a href="https://leetcode.com/problems/number-of-islands/"
           target="_blank" class="text-link">Number of Islands</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>201</td>
    <td><a href="https://leetcode.com/problems/bitwise-and-of-numbers-range/description/"
           target="_blank" class="text-link">Bitwise AND of Numbers Range</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>202</td>
    <td><a href="https://leetcode.com/problems/happy-number/description/"
           target="_blank" class="text-link">Happy Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>204</td>
    <td><a href="https://leetcode.com/problems/count-primes/description/"
           target="_blank" class="text-link">Count Primes</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>205</td>
    <td><a href="https://leetcode.com/problems/isomorphic-strings/description/"
           target="_blank" class="text-link">Isomorphic Strings</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>207</td>
    <td><a href="https://leetcode.com/problems/course-schedule/description/"
           target="_blank" class="text-link">Course Schedule</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>208</td>
    <td><a href="https://leetcode.com/problems/implement-trie-prefix-tree/description/"
           target="_blank" class="text-link">Implement Trie (Prefix Tree)
    </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>209</td>
    <td><a href="https://leetcode.com/problems/minimum-size-subarray-sum/description/"
           target="_blank" class="text-link">Minimum Size Subarray Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>210</td>
    <td><a href="https://leetcode.com/problems/course-schedule-ii/description/"
           target="_blank" class="text-link">Course Schedule II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>211</td>
    <td><a href="https://leetcode.com/problems/add-and-search-word-data-structure-design/description/"
           target="_blank" class="text-link">Add and Search Word - Data structure design
    </a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>212</td>
    <td><a href="https://leetcode.com/problems/word-search-ii/description/"
           target="_blank" class="text-link">Word Search II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>213</td>
    <td><a href="" target="_blank" class="text-link">House Robber II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>214</td>
    <td><a href="https://leetcode.com/problems/shortest-palindrome/description/"
           target="_blank" class="text-link">Shortest Palindrome</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>215</td>
    <td><a href="https://leetcode.com/problems/kth-largest-element-in-an-array/description/"
           target="_blank" class="text-link">Kth Largest Element in an Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>216</td>
    <td><a href="https://leetcode.com/problems/combination-sum-iii/description/"
           target="_blank" class="text-link">Combination Sum III</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>217</td>
    <td><a href="https://leetcode.com/problems/contains-duplicate/description/"
           target="_blank" class="text-link">Contains Duplicate</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>218</td>
    <td><a href="https://leetcode.com/problems/the-skyline-problem/description/"
           target="_blank" class="text-link"> The Skyline Problem</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>219</td>
    <td><a href="https://leetcode.com/problems/contains-duplicate-ii/description/"
           target="_blank" class="text-link">Contains Duplicate II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>220</td>
    <td><a href="https://leetcode.com/problems/contains-duplicate-iii/description/"
           target="_blank" class="text-link">Contains Duplicate III</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>221</td>
    <td><a href="https://leetcode.com/problems/maximal-square/description/"
           target="_blank" class="text-link">Maximal Square</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>224</td>
    <td><a href="https://leetcode.com/problems/basic-calculator/description/"
           target="_blank" class="text-link">Basic Calculator</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>225</td>
    <td><a href="https://leetcode.com/problems/implement-stack-using-queues/description/"
           target="_blank" class="text-link">Implement Stack using Queues</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>226</td>
    <td><a href="https://leetcode.com/problems/invert-binary-tree/description/"
           target="_blank" class="text-link">Invert Binary Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>227</td>
    <td><a href="https://leetcode.com/problems/basic-calculator-ii/description/"
           target="_blank" class="text-link">Basic Calculator II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>228</td>
    <td><a href="https://leetcode.com/problems/summary-ranges/description/"
           target="_blank" class="text-link">Summary Ranges</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>230</td>
    <td><a href="https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/"
           target="_blank" class="text-link">Kth Smallest Element in a BST</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>231</td>
    <td><a href="https://leetcode.com/problems/power-of-two/description/"
           target="_blank" class="text-link">Power of Two</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>232</td>
    <td><a href="https://leetcode.com/problems/implement-queue-using-stacks/description/"
           target="_blank" class="text-link">Implement Queue using Stacks</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>235</td>
    <td><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/"
           target="_blank" class="text-link">Lowest Common Ancestor of a Binary Search Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>236</td>
    <td><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/"
           target="_blank" class="text-link">Lowest Common Ancestor of a Binary Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>238</td>
    <td><a href="https://leetcode.com/problems/product-of-array-except-self/description/"
           target="_blank" class="text-link">Product of Array Except Self</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>239</td>
    <td><a href="https://leetcode.com/problems/sliding-window-maximum/description/"
           target="_blank" class="text-link">Sliding Window Maximum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>240</td>
    <td><a href="https://leetcode.com/problems/search-a-2d-matrix-ii/description/"
           target="_blank" class="text-link">Search a 2D Matrix II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>241</td>
    <td><a href="https://leetcode.com/problems/different-ways-to-add-parentheses/description/"
           target="_blank" class="text-link"> Different Ways to Add Parentheses</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>242</td>
    <td><a href="https://leetcode.com/problems/valid-anagram/description/"
           target="_blank" class="text-link">Valid Anagram</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>244</td>
    <td><a href="https://leetcode.com/problems/shortest-word-distance-ii/description/"
           target="_blank" class="text-link">Shortest Word Distance II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>245</td>
    <td><a href="https://leetcode.com/problems/shortest-word-distance-iii/description/" target="_blank" class="text-link">Shortest Word Distance III</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>249</td>
    <td><a href="https://leetcode.com/problems/group-shifted-strings/description/"
           target="_blank" class="text-link">Group Shifted Strings</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>251</td>
    <td><a href="https://leetcode.com/problems/flatten-2d-vector/description/s"
           target="_blank" class="text-link">Flatten 2D Vector</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>252</td>
    <td><a href="https://leetcode.com/problems/meeting-rooms/description/"
           target="_blank" class="text-link">Meeting Rooms</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>253</td>
    <td><a href="https://leetcode.com/problems/meeting-rooms-ii/description/"
           target="_blank" class="text-link">Meeting Rooms II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>254</td>
    <td><a href="https://leetcode.com/problems/factor-combinations/description/"
           target="_blank" class="text-link">Factor Combinations</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>256</td>
    <td><a href="https://leetcode.com/problems/paint-house/description/"
           target="_blank" class="text-link">Paint House</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>257</td>
    <td><a href="https://leetcode.com/problems/binary-tree-paths/description/"
           target="_blank" class="text-link">Binary Tree Paths</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>261</td>
    <td><a href="https://leetcode.com/problems/graph-valid-tree/description/"
           target="_blank" class="text-link">Graph Valid Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>263</td>
    <td><a href="https://leetcode.com/problems/ugly-number/description/"
           target="_blank" class="text-link">Ugly Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>264</td>
    <td><a href="https://leetcode.com/problems/ugly-number-ii/description/"
           target="_blank" class="text-link">Ugly Number II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>265</td>
    <td><a href="https://leetcode.com/problems/paint-house-ii/description/"
           target="_blank" class="text-link">Paint House II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>268</td>
    <td><a href="https://leetcode.com/problems/missing-number/description/"
           target="_blank" class="text-link">Missing Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>269</td>
    <td><a href="https://leetcode.com/problems/alien-dictionary/description/"
           target="_blank" class="text-link">Alien Dictionary</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>270</td>
    <td><a href="https://leetcode.com/problems/closest-binary-search-tree-value/description/"
           target="_blank" class="text-link">Closest Binary Search Tree Value</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>271</td>
    <td><a href="https://leetcode.com/problems/encode-and-decode-strings/description/"
           target="_blank" class="text-link">Encode and Decode Strings</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>273</td>
    <td><a href="https://leetcode.com/problems/integer-to-english-words/description/"
           target="_blank" class="text-link">Integer to English Words</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>274</td>
    <td><a href="https://leetcode.com/problems/h-index/description/"
           target="_blank" class="text-link">H-Index</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>275</td>
    <td><a href="https://leetcode.com/problems/h-index-ii/description/"
           target="_blank" class="text-link">H-Index II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>276</td>
    <td><a href="https://leetcode.com/problems/paint-fence/description/"
           target="_blank" class="text-link">Paint Fence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>277</td>
    <td><a href="https://leetcode.com/problems/find-the-celebrity/description/"
           target="_blank" class="text-link">Find the Celebrity</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>278</td>
    <td><a href="https://leetcode.com/problems/first-bad-version/description/"
           target="_blank" class="text-link"> First Bad Version</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>279</td>
    <td><a href="https://leetcode.com/problems/perfect-squares/description/"
           target="_blank" class="text-link">Perfect Squares</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>280</td>
    <td><a href="https://leetcode.com/problems/wiggle-sort/description/"
           target="_blank" class="text-link">Wiggle Sort</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>282</td>
    <td><a href="https://leetcode.com/problems/expression-add-operators/description/"
           target="_blank" class="text-link">Expression Add Operators</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>283</td>
    <td><a href="https://leetcode.com/problems/move-zeroes/description/"
           target="_blank" class="text-link">Move Zeroes</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>284</td>
    <td><a href="https://leetcode.com/problems/peeking-iterator/description/"
           target="_blank" class="text-link">Peeking Iterator</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>285</td>
    <td><a href="https://leetcode.com/problems/inorder-successor-in-bst/description/"
           target="_blank" class="text-link">Inorder Successor in BST</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>286</td>
    <td><a href="https://leetcode.com/problems/walls-and-gates/description/"
           target="_blank" class="text-link">Walls and Gates</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>287</td>
    <td><a href="https://leetcode.com/problems/find-the-duplicate-number/description/"
           target="_blank" class="text-link">Find the Duplicate Number</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>288</td>
    <td><a href="https://leetcode.com/problems/unique-word-abbreviation/description/"
           target="_blank" class="text-link">Unique Word Abbreviation</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>289</td>
    <td><a href="https://leetcode.com/problems/game-of-life/description/"
           target="_blank" class="text-link">Game of Life</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>290</td>
    <td><a href="https://leetcode.com/problems/word-pattern/description/"
           target="_blank" class="text-link">Word Pattern</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>291</td>
    <td><a href="https://leetcode.com/problems/word-pattern-ii/description/"
           target="_blank" class="text-link">Word Pattern II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>293</td>
    <td><a href="https://leetcode.com/problems/flip-game/description/"
           target="_blank" class="text-link">Flip Game</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>294</td>
    <td><a href="https://leetcode.com/problems/flip-game-ii/description/"
           target="_blank" class="text-link">Flip Game II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>295</td>
    <td><a href="https://leetcode.com/problems/find-median-from-data-stream/description/"
           target="_blank" class="text-link">Find Median from Data Stream</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>296</td>
    <td><a href="https://leetcode.com/problems/best-meeting-point/description/"
           target="_blank" class="text-link">Best Meeting Point</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>297</td>
    <td><a href="https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/"
           target="_blank" class="text-link">Serialize and Deserialize Binary Tree</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>298</td>
    <td><a href="https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/"
           target="_blank" class="text-link">Binary Tree Longest Consecutive Sequence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>299</td>
    <td><a href="https://leetcode.com/problems/bulls-and-cows/"
           target="_blank" class="text-link">Bulls and Cows</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>300</td>
    <td><a href="https://leetcode.com/problems/longest-increasing-subsequence/description/"
           target="_blank" class="text-link">Longest Increasing Subsequence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>301</td>
    <td><a href="https://leetcode.com/problems/remove-invalid-parentheses/description/"
           target="_blank" class="text-link">Remove Invalid Parentheses</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>302</td>
    <td><a href="https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/description/"
           target="_blank" class="text-link">Smallest Rectangle Enclosing Black Pixels</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>305</td>
    <td><a href="https://leetcode.com/problems/number-of-islands-ii/description/"
           target="_blank" class="text-link">Number of Islands II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>307</td>
    <td><a href="https://leetcode.com/problems/range-sum-query-mutable/description/"
           target="_blank" class="text-link">Range Sum Query - Mutable</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>308</td>
    <td><a href="https://leetcode.com/problems/range-sum-query-2d-mutable/description/"
           target="_blank" class="text-link">Range Sum Query 2D - Mutable</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>309</td>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/"
           target="_blank" class="text-link">Best Time to Buy and Sell Stock with Cooldown</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>311</td>
    <td><a href="https://leetcode.com/problems/sparse-matrix-multiplication/description/"
           target="_blank" class="text-link">Sparse Matrix Multiplication</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>312</td>
    <td><a href="https://leetcode.com/problems/burst-balloons/description/"
           target="_blank" class="text-link">Burst Balloons</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>314</td>
    <td><a href="https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/"
           target="_blank" class="text-link">Binary Tree Vertical Order Traversal</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>316</td>
    <td><a href="https://leetcode.com/problems/remove-duplicate-letters/description/"
           target="_blank" class="text-link">Remove Duplicate Letters</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>317</td>
    <td><a href="https://leetcode.com/problems/shortest-distance-from-all-buildings/description/"
           target="_blank" class="text-link">Shortest Distance from All Buildings</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>318</td>
    <td><a href="https://leetcode.com/problems/maximum-product-of-word-lengths/description/"
           target="_blank" class="text-link"> Maximum Product of Word Lengths</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>322</td>
    <td><a href="https://leetcode.com/problems/coin-change/description/"
           target="_blank" class="text-link">Coin Change</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>323</td>
    <td><a href="https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/"
           target="_blank" class="text-link">Number of Connected Components in an Undirected Graph</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>324</td>
    <td><a href="https://leetcode.com/problems/wiggle-sort-ii/description/"
           target="_blank" class="text-link"> Wiggle Sort II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>325</td>
    <td><a href="https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/"
           target="_blank" class="text-link">Maximum Size Subarray Sum Equals k</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>329</td>
    <td><a href="https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/"
           target="_blank" class="text-link">Longest Increasing Path in a Matrix</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>334</td>
    <td><a href="https://leetcode.com/problems/increasing-triplet-subsequence/description/"
           target="_blank" class="text-link">Increasing Triplet Subsequence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>336</td>
        <td><a href="https://leetcode.com/problems/palindrome-pairs/description/"
               target="_blank" class="text-link">Palindrome Pairs</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>337</td>
    <td><a href="https://leetcode.com/problems/house-robber-iii/description/"
           target="_blank" class="text-link">House Robber III</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>338</td>
    <td><a href="https://leetcode.com/problems/counting-bits/description/"
           target="_blank" class="text-link">Counting Bits</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>339</td>
    <td><a href="https://leetcode.com/problems/nested-list-weight-sum/description/"
           target="_blank" class="text-link">Nested List Weight Sum</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>340</td>
    <td><a href="https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/"
           target="_blank" class="text-link">Longest Substring with At Most K Distinct Characters</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>341</td>
    <td><a href="https://leetcode.com/problems/flatten-nested-list-iterator/"
           target="_blank" class="text-link">Flatten Nested List Iterator</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>346</td>
    <td><a href="https://leetcode.com/problems/moving-average-from-data-stream/description/"
           target="_blank" class="text-link">Moving Average from Data Stream</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>347</td>
    <td><a href="https://leetcode.com/problems/top-k-frequent-elements/description/"
           target="_blank" class="text-link">Top K Frequent Elements</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>348</td>
    <td><a href="https://leetcode.com/problems/design-tic-tac-toe/description/"
           target="_blank" class="text-link">Design Tic-Tac-Toe</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>350</td>
    <td><a href="https://leetcode.com/problems/intersection-of-two-arrays-ii/description/"
           target="_blank" class="text-link">Intersection of Two Arrays II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>351</td>
    <td><a href="https://leetcode.com/problems/android-unlock-patterns/description/"
           target="_blank" class="text-link">Android Unlock Patterns</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>352</td>
    <td><a href="https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/"
           target="_blank" class="text-link">Data Stream as Disjoint Intervals</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>353</td>
    <td><a href="https://leetcode.com/problems/design-snake-game/description/"
           target="_blank" class="text-link">Design Snake Game</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>354</td>
    <td><a href="https://leetcode.com/problems/russian-doll-envelopes/description/"
           target="_blank" class="text-link">Russian Doll Envelopes</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>355</td>
    <td><a href="https://leetcode.com/problems/design-twitter/description/s"
           target="_blank" class="text-link">Design Twitter</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>359</td>
    <td><a href="https://leetcode.com/problems/logger-rate-limiter/description/"
           target="_blank" class="text-link">Logger Rate Limiter</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>361</td>
    <td><a href="https://leetcode.com/problems/bomb-enemy/description/"
           target="_blank" class="text-link">Bomb Enemy</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>362</td>
    <td><a href="https://leetcode.com/problems/design-hit-counter/description/"
           target="_blank" class="text-link">Design Hit Counter</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>364</td>
    <td><a href="https://leetcode.com/problems/nested-list-weight-sum-ii/description/"
           target="_blank" class="text-link"> Nested List Weight Sum II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>367</td>
    <td><a href="https://leetcode.com/problems/valid-perfect-square/description/"
           target="_blank" class="text-link">Valid Perfect Square</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>374</td>
    <td><a href="https://leetcode.com/problems/guess-number-higher-or-lower/"
           target="_blank" class="text-link">Guess Number Higher or Lower</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>375</td>
    <td><a href="https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/"
           target="_blank" class="text-link"> Guess Number Higher or Lower II</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>376</td>
    <td><a href="https://leetcode.com/problems/wiggle-subsequence/description/"
           target="_blank" class="text-link">Wiggle Subsequence</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>377</td>
    <td><a href="https://leetcode.com/problems/combination-sum-iv/description/"
           target="_blank" class="text-link"> Combination Sum IV</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>378</td>
    <td><a href="https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/"
           target="_blank" class="text-link">Kth Smallest Element in a Sorted Matrix</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>379</td>
    <td><a href="https://leetcode.com/problems/design-phone-directory/description/"
           target="_blank" class="text-link">Design Phone Directory</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>380</td>
    <td><a href="https://leetcode.com/problems/insert-delete-getrandom-o1/"
           target="_blank" class="text-link">Insert Delete GetRandom O(1)</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>381</td>
    <td><a href="https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/"
           target="_blank" class="text-link">Insert Delete GetRandom O(1) - Duplicates allowed</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>384</td>
    <td><a href="https://leetcode.com/problems/shuffle-an-array/"
           target="_blank" class="text-link">Shuffle an Array</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>385</td>
    <td><a href="https://leetcode.com/problems/mini-parser/description/"
           target="_blank" class="text-link">Mini Parser</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>389</td>
    <td><a href="https://leetcode.com/problems/find-the-difference/description/"
           target="_blank" class="text-link">Find the Difference</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>394</td>
    <td><a href="https://leetcode.com/problems/decode-string/"
           target="_blank" class="text-link">Decode String</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>398</td>
    <td><a href="https://leetcode.com/problems/random-pick-index/"
           target="_blank" class="text-link">Random Pick Index</a></td>
        <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                        <!--Data Science 重点题目-->
                        <div class="tab-pane fade" id="nav-DSzhongdiantimu" role="tabpanel" aria-labelledby="nav-DSzhongdiantimu">
                            <div class="col-panel">
                                <div class="col-header">Data Science Leetcode 精简版</div>
                                <div class="col-body">
                                    <table class="table table-striped">
                                        <thead>
                                        <tr>
                                            <td>题号</td>
                                            <td>题目名称</td>
                                            <td>讲解链接</td>
                                            <td></td>
                                        </tr>
                                        </thead>
                                        <tbody>
<tr>
    <td>1</td>
    <td><a href="https://leetcode.com/problems/two-sum/description/"
           target="_blank" class="text-link">Two Sum</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>2</td>
    <td><a href="https://leetcode.com/problems/add-two-numbers/description/"
           target="_blank" class="text-link">Add Two Numbers</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>3</td>
    <td><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/description/"
           target="_blank" class="text-link">Longest Substring Without Repeating Characters</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>5</td>
    <td><a href="https://leetcode.com/problems/longest-palindromic-substring/description/"
           target="_blank" class="text-link">Longest Palindromic Substring
    </a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>7</td>
    <td><a href="https://leetcode.com/problems/reverse-integer/description/"
           target="_blank" class="text-link">Reverse Integer</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>8</td>
    <td><a href="https://leetcode.com/problems/string-to-integer-atoi/description/"
           target="_blank" class="text-link">String to Integer (atoi)</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>9</td>
    <td><a href="https://leetcode.com/problems/palindrome-number/description/" target="_blank"
           class="text-link">Palindrome Number</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>11</td>
    <td><a href="https://leetcode.com/problems/container-with-most-water/description/"
           target="_blank" class="text-link">Container With Most Water</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>14</td>
    <td><a href="https://leetcode.com/problems/longest-common-prefix/description/"
           target="_blank" class="text-link">Longest Common Prefix</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>15</td>
    <td><a href="https://leetcode.com/problems/3sum/description/"
           target="_blank" class="text-link">3Sum</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>16</td>
    <td><a href="https://leetcode.com/problems/3sum-closest/description/"
           target="_blank" class="text-link">3Sum Closest</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
</tr>
<tr>
    <td>17</td>
    <td><a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/"
           target="_blank" class="text-link">Letter Combinations of a Phone Number</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>18</td>
    <td><a href="https://leetcode.com/problems/4sum/description/"
           target="_blank" class="text-link">4Sum</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>19</td>
    <td><a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/"
           target="_blank" class="text-link">Remove Nth Node From End of List</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>20</td>
    <td><a href="https://leetcode.com/problems/valid-parentheses/description/"
           target="_blank" class="text-link">Valid Parentheses</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>21</td>
    <td><a href="https://leetcode.com/problems/merge-two-sorted-lists/description/"
           target="_blank" class="text-link">Merge Two Sorted Lists</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>22</td>
    <td><a href="https://leetcode.com/problems/generate-parentheses/description/"
           target="_blank" class="text-link">Generate Parentheses</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>24</td>
    <td><a href="https://leetcode.com/problems/swap-nodes-in-pairs/description/"
           target="_blank" class="text-link">Swap Nodes in Pairs</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>25</td>
    <td><a href="https://leetcode.com/problems/reverse-nodes-in-k-group/description/"
           target="_blank" class="text-link">Reverse Nodes in k-Group</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>26</td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/"
           target="_blank" class="text-link">Remove Duplicates from Sorted Array</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>27</td>
    <td><a href="https://leetcode.com/problems/remove-element/"
           target="_blank" class="text-link">Remove Element</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>

    <td></td>
</tr>
<tr>
    <td>28</td>
    <td><a href="https://leetcode.com/problems/implement-strstr/description/"
           target="_blank" class="text-link">Implement strStr()</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>29</td>
    <td><a href="https://leetcode.com/problems/divide-two-integers/description/"
           target="_blank" class="text-link">Divide Two Integers</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>30</td>
    <td><a href="https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/"
           target="_blank" class="text-link">Substring with Concatenation of All Words
    </a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
</tr>
<tr>
    <td>32</td>
    <td><a href="https://leetcode.com/problems/longest-valid-parentheses/description/"
           target="_blank" class="text-link">Longest Valid Parentheses</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>33</td>
    <td><a href="https://leetcode.com/problems/search-in-rotated-sorted-array/description/"
           target="_blank" class="text-link">Search in Rotated Sorted Array</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>35</td>
    <td><a href="https://leetcode.com/problems/search-insert-position/description/"
           target="_blank" class="text-link">Search Insert Position</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>36</td>
    <td><a href="https://leetcode.com/problems/valid-sudoku/description/"
           target="_blank" class="text-link">Valid Sudoku</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>39</td>
    <td><a href="https://leetcode.com/problems/combination-sum/description/"
           target="_blank" class="text-link">Combination Sum </a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>40</td>
    <td><a href="https://leetcode.com/problems/combination-sum-ii/description/"
           target="_blank" class="text-link">Combination Sum II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>41</td>
    <td><a href="https://leetcode.com/problems/first-missing-positive/description/"
           target="_blank" class="text-link">First Missing Positive</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>42</td>
    <td><a href="https://leetcode.com/problems/trapping-rain-water/description/"
           target="_blank" class="text-link">Trapping Rain Water</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>45</td>
    <td><a href="https://leetcode.com/problems/jump-game-ii/description/"
           target="_blank" class="text-link">Jump Game II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>46</td>
    <td><a href="https://leetcode.com/problems/permutations/description/"
           target="_blank" class="text-link">Permutations</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>47</td>
    <td><a href="https://leetcode.com/problems/permutations-ii/description/"
           target="_blank" class="text-link">Permutations II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>49</td>
    <td><a href="https://leetcode.com/problems/group-anagrams/description/"
           target="_blank" class="text-link">Group Anagrams</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>50</td>
    <td><a href="https://leetcode.com/problems/powx-n/description/" target="_blank"
           class="text-link">Pow(x, n)</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>53</td>
    <td><a href="https://leetcode.com/problems/maximum-subarray/description/"
           target="_blank" class="text-link">Maximum Subarray</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>55</td>
    <td><a href="https://leetcode.com/problems/jump-game/description/"
           target="_blank" class="text-link">Jump Game</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>56</td>
    <td><a href="https://leetcode.com/problems/merge-intervals/description/"
           target="_blank" class="text-link">Merge Intervals</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>57</td>
    <td><a href="https://leetcode.com/problems/insert-interval/description/"
           target="_blank" class="text-link">Insert Interval</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>58</td>
    <td><a href="https://leetcode.com/problems/length-of-last-word/description/"
           target="_blank" class="text-link">Length of Last Word</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>60</td>
    <td><a href="https://leetcode.com/problems/permutation-sequence/description/"
           target="_blank" class="text-link">Permutation Sequence</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>61</td>
    <td><a href="https://leetcode.com/problems/rotate-list/description/"
           target="_blank" class="text-link">Rotate List</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>62</td>
    <td><a href="https://leetcode.com/problems/unique-paths/description/"
           target="_blank" class="text-link">Unique Paths</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>63</td>
    <td><a href="https://leetcode.com/problems/unique-paths-ii/description/"
           target="_blank" class="text-link">Unique Paths II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>64</td>
    <td><a href="https://leetcode.com/problems/minimum-path-sum/description/"
           target="_blank" class="text-link"> Minimum Path Sum</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>66</td>
    <td><a href="https://leetcode.com/problems/plus-one/description/"
           target="_blank" class="text-link">Plus One</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>69</td>
    <td><a href="https://leetcode.com/problems/sqrtx/description/"
           target="_blank" class="text-link">Sqrt(x)</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>70</td>
    <td><a href="https://leetcode.com/problems/climbing-stairs/description/"
           target="_blank" class="text-link">Climbing Stairs</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>71</td>
    <td><a href="https://leetcode.com/problems/simplify-path/description/"
           target="_blank" class="text-link">Simplify Path</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>74</td>
    <td><a href="https://leetcode.com/problems/search-a-2d-matrix/description/"
           target="_blank" class="text-link">Search a 2D Matrix</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>75</td>
    <td><a href="https://leetcode.com/problems/sort-colors/description/"
           target="_blank" class="text-link">Sort Colors</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>76</td>
    <td><a href="https://leetcode.com/problems/minimum-window-substring/description/"
           target="_blank" class="text-link">Minimum Window Substring</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>77</td>
    <td><a href="https://leetcode.com/problems/combinations/description/"
           target="_blank" class="text-link">Combinations</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>78</td>
    <td><a href="https://leetcode.com/problems/subsets/description/"
           target="_blank" class="text-link">Subsets</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>79</td>
    <td><a href="https://leetcode.com/problems/word-search/description/"
           target="_blank" class="text-link">Word Search</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>80</td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/"
           target="_blank" class="text-link">Remove Duplicates from Sorted Array II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>82</td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/"
           target="_blank" class="text-link">Remove Duplicates from Sorted List II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>83</td>
    <td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/"
           target="_blank" class="text-link">Remove Duplicates from Sorted List</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>86</td>
    <td><a href="https://leetcode.com/problems/partition-list/description/"
           target="_blank" class="text-link">Partition List</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>87</td>
    <td><a href="https://leetcode.com/problems/scramble-string/description/"
           target="_blank" class="text-link">Scramble String</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>88</td>
    <td><a href="https://leetcode.com/problems/merge-sorted-array/description/"
           target="_blank" class="text-link">Merge Sorted Array</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>90</td>
    <td><a href="https://leetcode.com/problems/subsets-ii/description/"
           target="_blank" class="text-link">Subsets II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>92</td>
    <td><a href="https://leetcode.com/problems/reverse-linked-list-ii/description/"
           target="_blank" class="text-link">Reverse Linked List II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>94</td>
    <td><a href="https://leetcode.com/problems/binary-tree-inorder-traversal/description/"
           target="_blank" class="text-link">Binary Tree Inorder Traversal</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>98</td>
    <td><a href="https://leetcode.com/problems/validate-binary-search-tree/description/"
           target="_blank" class="text-link">Validate Binary Search Tree</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>99</td>
    <td><a href="https://leetcode.com/problems/recover-binary-search-tree/"
           target="_blank" class="text-link">Recover Binary Search Tree</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
</tr>

<tr>
    <td>100</td>
    <td><a href="https://leetcode.com/problems/same-tree/description/"
           target="_blank" class="text-link">Same Tree</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>101</td>
    <td><a href="https://leetcode.com/problems/symmetric-tree/description/"
           target="_blank" class="text-link">Symmetric Tree</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>102</td>
    <td><a href="https://leetcode.com/problems/binary-tree-level-order-traversal/description/"
           target="_blank" class="text-link">Binary Tree Level Order Traversal</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>103</td>
    <td><a href="https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/"
           target="_blank" class="text-link">Binary Tree Zigzag Level Order Traversal</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>104</td>
    <td><a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/description/"
           target="_blank" class="text-link">Maximum Depth of Binary Tree</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>107</td>
    <td><a href="https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/"
           target="_blank" class="text-link">Binary Tree Level Order Traversal II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>110</td>
    <td><a href="https://leetcode.com/problems/balanced-binary-tree/description/"
           target="_blank" class="text-link">Balanced Binary Tree</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>111</td>
    <td><a href="https://leetcode.com/problems/minimum-depth-of-binary-tree/description/"
           target="_blank" class="text-link">Minimum Depth of Binary Tree</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>112</td>
    <td><a href="https://leetcode.com/problems/path-sum/description/" target="_blank" class="text-link">Path Sum</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>113</td>
    <td><a href="https://leetcode.com/problems/path-sum-ii/description/"
           target="_blank" class="text-link">Path Sum II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>121</td>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/"
           target="_blank" class="text-link">Best Time to Buy and Sell Stock</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>122</td>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/"
           target="_blank" class="text-link"> Best Time to Buy and Sell Stock II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>124</td>
    <td><a href="https://leetcode.com/problems/binary-tree-maximum-path-sum/description/"
           target="_blank" class="text-link">Binary Tree Maximum Path Sum</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>125</td>
    <td><a href="https://leetcode.com/problems/valid-palindrome/description/"
           target="_blank" class="text-link">Valid Palindrome</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>127</td>
    <td><a href="https://leetcode.com/problems/word-ladder/description/"
           target="_blank" class="text-link"> Word Ladder</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>129</td>
    <td><a href="https://leetcode.com/problems/sum-root-to-leaf-numbers/description/"
           target="_blank" class="text-link">Sum Root to Leaf Numbers</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>131</td>
    <td><a href="https://leetcode.com/problems/palindrome-partitioning/description/"
           target="_blank" class="text-link">Palindrome Partitioning</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>136</td>
    <td><a href="https://leetcode.com/problems/single-number/description/"
           target="_blank" class="text-link">Single Number</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>138</td>
    <td><a href="https://leetcode.com/problems/copy-list-with-random-pointer/"
           target="_blank" class="text-link">Copy List with Random Pointer</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>139</td>
    <td><a href="https://leetcode.com/problems/word-break/"
           target="_blank" class="text-link">Word Break</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>141</td>
    <td><a href="https://leetcode.com/problems/linked-list-cycle/description/"
           target="_blank" class="text-link">Linked List Cycle</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>142</td>
    <td><a href="https://leetcode.com/problems/linked-list-cycle-ii/description/"
           target="_blank" class="text-link">Linked List Cycle II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>143</td>
    <td><a href="https://leetcode.com/problems/reorder-list/description/"
           target="_blank" class="text-link">Reorder List</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>144</td>
    <td><a href="https://leetcode.com/problems/binary-tree-preorder-traversal/description/"
           target="_blank" class="text-link">Binary Tree Preorder Traversal</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>145</td>
    <td><a href="https://leetcode.com/problems/binary-tree-postorder-traversal/description/"
           target="_blank" class="text-link">Binary Tree Postorder Traversal</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>148</td>
    <td><a href="https://leetcode.com/problems/sort-list/description/"
           target="_blank" class="text-link">Sort List</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>150</td>
    <td><a href="https://leetcode.com/problems/evaluate-reverse-polish-notation/description/"
           target="_blank" class="text-link">Evaluate Reverse Polish Notation</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>151</td>
    <td><a href="https://leetcode.com/problems/reverse-words-in-a-string/description/"
           target="_blank" class="text-link">Reverse Words in a String</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>153</td>
    <td><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/"
           target="_blank" class="text-link">Find Minimum in Rotated Sorted Array</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>154</td>
    <td><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/"
           target="_blank" class="text-link">Find Minimum in Rotated Sorted Array II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>155</td>
    <td><a href="https://leetcode.com/problems/min-stack/description/"
           target="_blank" class="text-link">Min Stack</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>

<tr>
    <td>156</td>
    <td><a href="https://leetcode.com/problems/binary-tree-upside-down/description/"
           target="_blank" class="text-link"> Binary Tree Upside Down</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
</tr>
<tr>
    <td>160</td>
    <td><a href="https://leetcode.com/problems/intersection-of-two-linked-lists/description/"
           target="_blank" class="text-link">Intersection of Two Linked Lists</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>161</td>
    <td><a href="https://leetcode.com/problems/one-edit-distance/"
           target="_blank" class="text-link">One Edit Distance</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>162</td>
    <td><a href="https://leetcode.com/problems/find-peak-element/description/"
           target="_blank" class="text-link">Find Peak Element </a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>163</td>
    <td><a href="https://leetcode.com/problems/missing-ranges/description/"
           target="_blank" class="text-link">Missing Ranges</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>165</td>
    <td><a href="https://leetcode.com/problems/compare-version-numbers/description/"
           target="_blank" class="text-link">Compare Version Numbers</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>167</td>
    <td><a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/"
           target="_blank" class="text-link">Two Sum II - Input array is sorted</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>168</td>
    <td><a href="https://leetcode.com/problems/excel-sheet-column-title/description/"
           target="_blank" class="text-link">Excel Sheet Column Title</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>169</td>
    <td><a href="https://leetcode.com/problems/majority-element/description/"
           target="_blank" class="text-link">Majority Element</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
</tr>
<tr>
    <td>170</td>
    <td><a href="https://leetcode.com/problems/two-sum-iii-data-structure-design/description/"
           target="_blank" class="text-link">Two Sum III - Data structure design</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>171</td>
    <td><a href="https://leetcode.com/problems/excel-sheet-column-number/description/"
           target="_blank" class="text-link">Excel Sheet Column Number</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>173</td>
    <td><a href="https://leetcode.com/problems/binary-search-tree-iterator/description/"
           target="_blank" class="text-link">Binary Search Tree Iterator</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>186</td>
    <td><a href="https://leetcode.com/problems/reverse-words-in-a-string-ii/description/"
           target="_blank" class="text-link">Reverse Words in a String II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>187</td>
    <td><a href="https://leetcode.com/problems/repeated-dna-sequences/description/"
           target="_blank" class="text-link">Repeated DNA Sequences</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
</tr>
<tr>
    <td>198</td>
    <td><a href="https://leetcode.com/problems/house-robber/"
           target="_blank" class="text-link">House Robber</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>199</td>
    <td><a href="https://leetcode.com/problems/binary-tree-right-side-view/description/"
           target="_blank" class="text-link">Binary Tree Right Side View</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
</tr>
<tr>
    <td>200</td>
    <td><a href="https://leetcode.com/problems/number-of-islands/"
           target="_blank" class="text-link">Number of Islands</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>202</td>
    <td><a href="https://leetcode.com/problems/happy-number/description/"
           target="_blank" class="text-link">Happy Number</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>203</td>
    <td><a href="https://leetcode.com/problems/remove-linked-list-elements/description/"
           target="_blank" class="text-link">Remove Linked List Elements</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>205</td>
    <td><a href="https://leetcode.com/problems/isomorphic-strings/description/"
           target="_blank" class="text-link">Isomorphic Strings</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>206</td>
    <td><a href="https://leetcode.com/problems/reverse-linked-list/description/"
           target="_blank" class="text-link">Reverse Linked List</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>209</td>
    <td><a href="https://leetcode.com/problems/minimum-size-subarray-sum/description/"
           target="_blank" class="text-link">Minimum Size Subarray Sum</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>213</td>
    <td><a href="" target="_blank" class="text-link">House Robber II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>214</td>
    <td><a href="https://leetcode.com/problems/shortest-palindrome/description/"
           target="_blank" class="text-link">Shortest Palindrome</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>215</td>
    <td><a href="https://leetcode.com/problems/kth-largest-element-in-an-array/description/"
           target="_blank" class="text-link">Kth Largest Element in an Array</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>216</td>
    <td><a href="https://leetcode.com/problems/combination-sum-iii/description/"
           target="_blank" class="text-link">Combination Sum III</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>217</td>
    <td><a href="https://leetcode.com/problems/contains-duplicate/description/"
           target="_blank" class="text-link">Contains Duplicate</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>219</td>
    <td><a href="https://leetcode.com/problems/contains-duplicate-ii/description/"
           target="_blank" class="text-link">Contains Duplicate II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>220</td>
    <td><a href="https://leetcode.com/problems/contains-duplicate-iii/description/"
           target="_blank" class="text-link">Contains Duplicate III</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>221</td>
    <td><a href="https://leetcode.com/problems/maximal-square/description/"
           target="_blank" class="text-link">Maximal Square</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>224</td>
    <td><a href="https://leetcode.com/problems/basic-calculator/description/"
           target="_blank" class="text-link">Basic Calculator</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>225</td>
    <td><a href="https://leetcode.com/problems/implement-stack-using-queues/description/"
           target="_blank" class="text-link">Implement Stack using Queues</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>226</td>
    <td><a href="https://leetcode.com/problems/invert-binary-tree/description/"
           target="_blank" class="text-link">Invert Binary Tree</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>227</td>
    <td><a href="https://leetcode.com/problems/basic-calculator-ii/description/"
           target="_blank" class="text-link">Basic Calculator II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>228</td>
    <td><a href="https://leetcode.com/problems/summary-ranges/description/"
           target="_blank" class="text-link">Summary Ranges</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>229</td>
    <td><a href="https://leetcode.com/problems/majority-element-ii/description/"
           target="_blank" class="text-link">Majority Element II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
</tr>
<tr>
    <td>230</td>
    <td><a href="https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/"
           target="_blank" class="text-link">Kth Smallest Element in a BST</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>232</td>
    <td><a href="https://leetcode.com/problems/implement-queue-using-stacks/description/"
           target="_blank" class="text-link">Implement Queue using Stacks</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>234</td>
    <td><a href="https://leetcode.com/problems/palindrome-linked-list/description/"
           target="_blank" class="text-link"> Palindrome Linked List</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>235</td>
    <td><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/"
           target="_blank" class="text-link">Lowest Common Ancestor of a Binary Search Tree</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>236</td>
    <td><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/"
           target="_blank" class="text-link">Lowest Common Ancestor of a Binary Tree</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>237</td>
    <td><a href="https://leetcode.com/problems/delete-node-in-a-linked-list/description/"
           target="_blank" class="text-link">Delete Node in a Linked List</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>238</td>
    <td><a href="https://leetcode.com/problems/product-of-array-except-self/description/"
           target="_blank" class="text-link">Product of Array Except Self</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>239</td>
    <td><a href="https://leetcode.com/problems/sliding-window-maximum/description/"
           target="_blank" class="text-link">Sliding Window Maximum</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>240</td>
    <td><a href="https://leetcode.com/problems/search-a-2d-matrix-ii/description/"
           target="_blank" class="text-link">Search a 2D Matrix II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>242</td>
    <td><a href="https://leetcode.com/problems/valid-anagram/description/"
           target="_blank" class="text-link">Valid Anagram</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>243</td>
    <td><a href="https://leetcode.com/problems/shortest-word-distance/description/"
           target="_blank" class="text-link">Shortest Word Distance</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>244</td>
    <td><a href="https://leetcode.com/problems/shortest-word-distance-ii/description/"
           target="_blank" class="text-link">Shortest Word Distance II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>245</td>
    <td><a href="https://leetcode.com/problems/shortest-word-distance-iii/description/" target="_blank" class="text-link">Shortest Word Distance III</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>246</td>
    <td><a href="https://leetcode.com/problems/strobogrammatic-number/description/"
           target="_blank" class="text-link">Strobogrammatic Number</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>247</td>
    <td><a href="https://leetcode.com/problems/strobogrammatic-number-ii/description/"
           target="_blank" class="text-link">Strobogrammatic Number II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>250</td>
    <td><a href="https://leetcode.com/problems/count-univalue-subtrees/description/"
           target="_blank" class="text-link">Count Univalue Subtrees</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>251</td>
    <td><a href="https://leetcode.com/problems/flatten-2d-vector/description/s"
           target="_blank" class="text-link">Flatten 2D Vector</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>252</td>
    <td><a href="https://leetcode.com/problems/meeting-rooms/description/"
           target="_blank" class="text-link">Meeting Rooms</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>253</td>
    <td><a href="https://leetcode.com/problems/meeting-rooms-ii/description/"
           target="_blank" class="text-link">Meeting Rooms II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>254</td>
    <td><a href="https://leetcode.com/problems/factor-combinations/description/"
           target="_blank" class="text-link">Factor Combinations</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>255</td>
    <td><a href="https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/"
           target="_blank" class="text-link">Verify Preorder Sequence in Binary Search Tree</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
</tr>
<tr>
    <td>256</td>
    <td><a href="https://leetcode.com/problems/paint-house/description/"
           target="_blank" class="text-link">Paint House</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>257</td>
    <td><a href="https://leetcode.com/problems/binary-tree-paths/description/"
           target="_blank" class="text-link">Binary Tree Paths</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>258</td>
    <td><a href="https://leetcode.com/problems/add-digits/description/"
           target="_blank" class="text-link"> Add Digits</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>259</td>
    <td><a href="https://leetcode.com/problems/3sum-smaller/description/"
           target="_blank" class="text-link">3Sum Smaller</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
</tr>
<tr>
    <td>263</td>
    <td><a href="https://leetcode.com/problems/ugly-number/description/"
           target="_blank" class="text-link">Ugly Number</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>264</td>
    <td><a href="https://leetcode.com/problems/ugly-number-ii/description/"
           target="_blank" class="text-link">Ugly Number II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>266</td>
    <td><a href="https://leetcode.com/problems/palindrome-permutation/description/"
           target="_blank" class="text-link">Palindrome Permutation</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>267</td>
    <td><a href="https://leetcode.com/problems/palindrome-permutation-ii/description/"
           target="_blank" class="text-link">Palindrome Permutation II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>268</td>
    <td><a href="https://leetcode.com/problems/missing-number/description/"
           target="_blank" class="text-link">Missing Number</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>270</td>
    <td><a href="https://leetcode.com/problems/closest-binary-search-tree-value/description/"
           target="_blank" class="text-link">Closest Binary Search Tree Value</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>274</td>
    <td><a href="https://leetcode.com/problems/h-index/description/"
           target="_blank" class="text-link">H-Index</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>275</td>
    <td><a href="https://leetcode.com/problems/h-index-ii/description/"
           target="_blank" class="text-link">H-Index II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>277</td>
    <td><a href="https://leetcode.com/problems/find-the-celebrity/description/"
           target="_blank" class="text-link">Find the Celebrity</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>278</td>
    <td><a href="https://leetcode.com/problems/first-bad-version/description/"
           target="_blank" class="text-link"> First Bad Version</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>279</td>
    <td><a href="https://leetcode.com/problems/perfect-squares/description/"
           target="_blank" class="text-link">Perfect Squares</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>280</td>
    <td><a href="https://leetcode.com/problems/wiggle-sort/description/"
           target="_blank" class="text-link">Wiggle Sort</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>283</td>
    <td><a href="https://leetcode.com/problems/move-zeroes/description/"
           target="_blank" class="text-link">Move Zeroes</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>285</td>
    <td><a href="https://leetcode.com/problems/inorder-successor-in-bst/description/"
           target="_blank" class="text-link">Inorder Successor in BST</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>286</td>
    <td><a href="https://leetcode.com/problems/walls-and-gates/description/"
           target="_blank" class="text-link">Walls and Gates</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>287</td>
    <td><a href="https://leetcode.com/problems/find-the-duplicate-number/description/"
           target="_blank" class="text-link">Find the Duplicate Number</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>288</td>
    <td><a href="https://leetcode.com/problems/unique-word-abbreviation/description/"
           target="_blank" class="text-link">Unique Word Abbreviation</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>290</td>
    <td><a href="https://leetcode.com/problems/word-pattern/description/"
           target="_blank" class="text-link">Word Pattern</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>295</td>
    <td><a href="https://leetcode.com/problems/find-median-from-data-stream/description/"
           target="_blank" class="text-link">Find Median from Data Stream</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>296</td>
    <td><a href="https://leetcode.com/problems/best-meeting-point/description/"
           target="_blank" class="text-link">Best Meeting Point</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>298</td>
    <td><a href="https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/"
           target="_blank" class="text-link">Binary Tree Longest Consecutive Sequence</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>299</td>
    <td><a href="https://leetcode.com/problems/bulls-and-cows/"
           target="_blank" class="text-link">Bulls and Cows</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>300</td>
    <td><a href="https://leetcode.com/problems/longest-increasing-subsequence/description/"
           target="_blank" class="text-link">Longest Increasing Subsequence</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>303</td>
    <td><a href="https://leetcode.com/problems/range-sum-query-immutable/description/"
           target="_blank" class="text-link">Range Sum Query - Immutable</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>304</td>
    <td><a href="https://leetcode.com/problems/range-sum-query-2d-immutable/description/"
           target="_blank" class="text-link">Range Sum Query 2D - Immutable</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>305</td>
    <td><a href="https://leetcode.com/problems/number-of-islands-ii/description/"
           target="_blank" class="text-link">Number of Islands II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>311</td>
    <td><a href="https://leetcode.com/problems/sparse-matrix-multiplication/description/"
           target="_blank" class="text-link">Sparse Matrix Multiplication</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>313</td>
    <td><a href="https://leetcode.com/problems/super-ugly-number/description/"
           target="_blank" class="text-link">Super Ugly Number</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
</tr>
<tr>
    <td>316</td>
    <td><a href="https://leetcode.com/problems/remove-duplicate-letters/description/"
           target="_blank" class="text-link">Remove Duplicate Letters</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>320</td>
    <td><a href="https://leetcode.com/problems/generalized-abbreviation/description/"
           target="_blank" class="text-link">Generalized Abbreviation</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>322</td>
    <td><a href="https://leetcode.com/problems/coin-change/description/"
           target="_blank" class="text-link">Coin Change</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>325</td>
    <td><a href="https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/"
           target="_blank" class="text-link">Maximum Size Subarray Sum Equals k</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>326</td>
    <td><a href="https://leetcode.com/problems/power-of-three/description/"
           target="_blank" class="text-link"> Power of Three</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>328</td>
    <td><a href="https://leetcode.com/problems/odd-even-linked-list/description/"
           target="_blank" class="text-link">Odd Even Linked List</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>330</td>
    <td><a href="https://leetcode.com/problems/patching-array/description/"
           target="_blank" class="text-link">Patching Array</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
</tr>
<tr>
    <td>334</td>
    <td><a href="https://leetcode.com/problems/increasing-triplet-subsequence/description/"
           target="_blank" class="text-link">Increasing Triplet Subsequence</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>337</td>
    <td><a href="https://leetcode.com/problems/house-robber-iii/description/"
           target="_blank" class="text-link">House Robber III</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>339</td>
    <td><a href="https://leetcode.com/problems/nested-list-weight-sum/description/"
           target="_blank" class="text-link">Nested List Weight Sum</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>340</td>
    <td><a href="https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/"
           target="_blank" class="text-link">Longest Substring with At Most K Distinct Characters</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>341</td>
    <td><a href="https://leetcode.com/problems/flatten-nested-list-iterator/"
           target="_blank" class="text-link">Flatten Nested List Iterator</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>342</td>
    <td><a href="https://leetcode.com/problems/power-of-four/description/"
           target="_blank" class="text-link">Power of Four</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>344</td>
    <td><a href="https://leetcode.com/problems/reverse-string/description/"
           target="_blank" class="text-link">Reverse String</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>345</td>
    <td><a href="https://leetcode.com/problems/reverse-vowels-of-a-string/description/"
           target="_blank" class="text-link">Reverse Vowels of a String</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>346</td>
    <td><a href="https://leetcode.com/problems/moving-average-from-data-stream/description/"
           target="_blank" class="text-link">Moving Average from Data Stream</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>347</td>
    <td><a href="https://leetcode.com/problems/top-k-frequent-elements/description/"
           target="_blank" class="text-link">Top K Frequent Elements</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>349</td>
    <td><a href="https://leetcode.com/problems/intersection-of-two-arrays/description/"
           target="_blank" class="text-link">Intersection of Two Arrays</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>350</td>
    <td><a href="https://leetcode.com/problems/intersection-of-two-arrays-ii/description/"
           target="_blank" class="text-link">Intersection of Two Arrays II</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>356</td>
    <td><a href="https://leetcode.com/problems/line-reflection/description/"
           target="_blank" class="text-link">Line Reflection</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
</tr>
<tr>
    <td>359</td>
    <td><a href="https://leetcode.com/problems/logger-rate-limiter/description/"
           target="_blank" class="text-link">Logger Rate Limiter</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>360</td>
    <td><a href="https://leetcode.com/problems/sort-transformed-array/description/"
           target="_blank" class="text-link">Sort Transformed Array</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>362</td>
    <td><a href="https://leetcode.com/problems/design-hit-counter/description/"
           target="_blank" class="text-link">Design Hit Counter</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>365</td>
    <td><a href="https://leetcode.com/problems/water-and-jug-problem/description/"
           target="_blank" class="text-link">Water and Jug Problem</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>366</td>
    <td><a href="https://leetcode.com/problems/find-leaves-of-binary-tree/description/"
           target="_blank" class="text-link">Find Leaves of Binary Tree</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>367</td>
    <td><a href="https://leetcode.com/problems/valid-perfect-square/description/"
           target="_blank" class="text-link">Valid Perfect Square</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>369</td>
    <td><a href="https://leetcode.com/problems/plus-one-linked-list/description/"
           target="_blank" class="text-link">Plus One Linked List</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>370</td>
    <td><a href="https://leetcode.com/problems/range-addition/description/"
           target="_blank" class="text-link">Range Addition</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>373</td>
    <td><a href="https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/"
           target="_blank" class="text-link">Find K Pairs with Smallest Sums</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
</tr>
<tr>
    <td>374</td>
    <td><a href="https://leetcode.com/problems/guess-number-higher-or-lower/"
           target="_blank" class="text-link">Guess Number Higher or Lower</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>376</td>
    <td><a href="https://leetcode.com/problems/wiggle-subsequence/description/"
           target="_blank" class="text-link">Wiggle Subsequence</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>377</td>
    <td><a href="https://leetcode.com/problems/combination-sum-iv/description/"
           target="_blank" class="text-link"> Combination Sum IV</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>378</td>
    <td><a href="https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/"
           target="_blank" class="text-link">Kth Smallest Element in a Sorted Matrix</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>379</td>
    <td><a href="https://leetcode.com/problems/design-phone-directory/description/"
           target="_blank" class="text-link">Design Phone Directory</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>380</td>
    <td><a href="https://leetcode.com/problems/insert-delete-getrandom-o1/"
           target="_blank" class="text-link">Insert Delete GetRandom O(1)</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>381</td>
    <td><a href="https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/"
           target="_blank" class="text-link">Insert Delete GetRandom O(1) - Duplicates allowed</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>383</td>
    <td><a href="https://leetcode.com/problems/ransom-note/description/"
           target="_blank" class="text-link">Ransom Note</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>387</td>
    <td><a href="https://leetcode.com/problems/first-unique-character-in-a-string/description/"
           target="_blank" class="text-link">First Unique Character in a String</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>388</td>
    <td><a href="https://leetcode.com/problems/longest-absolute-file-path/description/"
           target="_blank" class="text-link">Longest Absolute File Path</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>389</td>
    <td><a href="https://leetcode.com/problems/find-the-difference/description/"
           target="_blank" class="text-link">Find the Difference</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>392</td>
    <td><a href="https://leetcode.com/problems/is-subsequence/description/"
           target="_blank" class="text-link">Is Subsequence</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>
<tr>
    <td>400</td>
    <td><a href="https://leetcode.com/problems/nth-digit/description/"
           target="_blank" class="text-link">Nth Digit</a></td>
    <td><a href="/login" class="text-link">视频讲解</a></td>
    <td></td>
</tr>                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                        <div class="tab-pane fade" id="nav-about" role="tabpanel" aria-labelledby="nav-about-tab">
                            <div class="col-panel">
                                <div class="col-header">Edward Shi</div>
                                <div class="col-body">
                                    <div class="col-cell">
                                        <div class="cell-body">
                                            <div class="cell-intro">
                                                <p>留学两年多，刷题过三千。</p>
                                                <p>CS科班出身，但非ACMer，从没接触过ACM。从树的遍历捡起算法，纯自己刷题。</p>
                                                <p>在北美留学期间刷了3000多道题，全部都是Leetcode和面试题。自我总结出公司面试题出题方式，套路。</p>
                                                <p>独立做出针对面试刷题的课程，课程如下：</p>
                                                <p>《算法基础知识（上下）》</p>
                                                <p>《题型技巧总结（上下）》</p>
                                                <p>《Leetcode 题目视频讲解（上中下1-900题）》</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!--微信交流群-->
                        <div class="tab-pane fade" id="nav-weixinjiaoliuqun" role="tabpanel" aria-labelledby="nav-weixinjiaoliuqun">
                            <div class="col-panel">
                                <div class="col-header">北美CS刷题求职群</div>
                                <div class="col-body">
                                    <div class="row row-wx">
                                        <div class="col-lg-4">
                                            <div class="col-wx">
                                                <img src="/common/images/小助手.png" height="150px" width="150px" alt="" />
                                                <p>-北美CS刷题求职群-<br /><span>实习全职百人大群</span></p>
                                            </div>
                                        </div>
                                        <div class="col-lg-4">
                                            <div class="col-wx">
                                                <img src="/common/images/Cspiration服务号.jpg" height="150px" width="150px" alt="" />
                                                <p>-Cspiration官方公众号-<br/><span>每周第一手求职信息</span></p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!--参考网站-->
                        <div class="tab-pane fade" id="nav-cankaowangzhan" role="tabpanel" aria-labelledby="nav-cankaowangzhan">
                            <div class="col-panel">
                                <div class="col-header">LeetCode</div>
                                <div class="col-body">
                                    <div class="cell-intro">
                                        ​https://leetcode.com
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- 全⽹网唯一的刷题体系 -->
<div class="section" style="padding-top: 10px">
    <div class="sec-header">
        <h3><span>全网唯一 刷题体系</span></h3>
        <p>三大课程，从算法小白，到可以“横扫”各大国内外公司，让FMAG不是梦</p>
    </div>
    <div class="container">
        <div class="tx-row justify">
            <div class="kc-card">
                <div class="kc-photo">
                    <a href="/algorithmFoundation"><img src="/common/images/ke1.jpg" alt="" /></a>
                </div>
                <a class="kc-intro">
                    <div class="kc-tit">算法基础知识</div>
                    <div class="kc-desc">Java 零基础学起，一天搞定，数据结构实现，Java 源码分析，Leetcode 实战结合</div>
                </a>
            </div>
            <div class="arrow"><img src="/common/images/arrw.png" alt="" /></div>
            <div class="kc-card">
                <div class="kc-photo">
                    <a href="/algorithmSkills"><img src="/common/images/ke2.jpg" alt="" /></a>
                </div>
                <a class="kc-intro">
                    <div class="kc-tit">题型技巧总结</div>
                    <div class="kc-desc">3000题方法总结，套路模版汇总，独家方法，瞬间想出思路</div>
                </a>
            </div>
            <div class="arrow"><img src="/common/images/arrw.png" alt="" /></div>
            <div class="kc-card">
                <div class="kc-photo">
                    <a href="/leetCodeCourse"><img src="/common/images/ke3.jpg" alt="" /></a>
                </div>
                <a class="kc-intro">
                    <div class="kc-tit">LeetCode 题目视频讲解</div>
                    <div class="kc-desc">全网唯一，刷题必买，一题多解最优解，初学者即可一天10题，有刷题经验一天30题</div>
                </a>
            </div>
        </div>
    </div>
</div>
</div>
<footer class="footer">
    <div class="container">
        <div class="row foot-row">
            <div class="col col-info">
                <div class="end-logo">
                    <img src="/common/images/CSON.png" width="214px" height="70px" alt="" />
                </div>
                <div class="end-link">
                    <h4>CSPIRATION</h4>
                    <p><a href="/legal/privacy">隐私政策</a></p>
                    <p><a href="/legal/user-agreement">用户协议</a></p>
                    <p><a href="/legal/copyright">版权保护</a></p>
                    <p><a href="/legal/security">网站安全</a></p>
                    <p><a href="/legal/referral">内推人计划</a></p>
                </div>
                <div class="end-text">
                    <h4>联系我们</h4>
                    <p>Emaill:<br />admin@cspiration.com</p>
                </div>
            </div>
            <div class="col-6">
                <ul class="wx-list list-unstyled">
                    <li>
                        <img src="/common/images/小助手.png" height="150px" width="150px" alt="" />
                        <p>-北美CS刷题求职群-<br /><span>实习全职百人大群</span></p>
                    </li>
                    <li>
                        <img src="/common/images/Cspiration服务号.jpg" alt="" />
                        <p>-Cspiration官方公众号-<br /><span>每周第一手求职信息</span></p>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</footer>
    <!--咨询-->
    <div class="wx-popover">
        <div class="pp-header"></div>
        <div class="pp-body">
            <img src="/common/images/客服微信.jpeg" alt="" />
            <div class="t">扫描微信二维码<br />课程和网站疑问</div>
            <div class="g">针对课程有疑问？<br />购买时遇到问题？</div>
        </div>
    </div>
    <script src="/common/js/jquery.min.js"></script>
    <script src="/common/js/bootstrap.min.js"></script>
    <script src="/common/js/jquery.nav.js"></script>
    <script src="/common/js/owl.carousel.min.js"></script>
    <script src="/common/js/main.js"></script>
    <script src="/common/js/windows.js"></script>
    <script src="/common/js/toastr.js"></script>
    <script src="/common/js/scroll.js"></script>
<script type="text/javascript">

    $('.tab-cell').click(function() {
        var par = $(this).parents('li')
        par.toggleClass('open')
        par.find('.sec-navbar').slideToggle('fast')
    })
    $('.nav-link').click(function(){
        $('.nav-link').removeClass('active').removeClass('show')

    })
</script>
<script type="text/javascript">
    function compile(){

        //获取要转换的文字
        var text = document.getElementById("content").value;
        //创建实例
        var converter = new showdown.Converter();
        //进行转换
        var html = converter.makeHtml(text);
        //展示到对应的地方  result便是id名称
        document.getElementById("result").innerHTML = html;
    }
    compile()
</script>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
for tr in soup.find_all('tr'):
    text = tr.get_text()
    l = text.split('\n')
    new_s = "- [ ] " + l[1] + " " + l[2] + " " + l[4]
    if (l[1][0] > '0' and l[1][0] < '9'):
    	print(new_s)
