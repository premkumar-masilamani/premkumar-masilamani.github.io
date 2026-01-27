---
layout: post
lang: english
type: blog
permalink: /english/blog/:title/

date: 2013-11-21
title: A Goodbye Email from a Hardcore Programmer
---

I quit TCS. Today is my last day. I wanted my final goodbye email to be very special, unique and resemble what I did in TCS. This is what I sent to my colleagues today :)

<style>
  /* Scope EVERYTHING to .code-block */
  .code-block {
    background: #ffffff;
    border: 1px solid #000;
    padding: 16px;
    overflow-x: auto;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas,
                 "Liberation Mono", monospace;
    font-size: 10pt;
    line-height: 1.4;
    color: #000;
    white-space: pre;
  }

  /* Syntax colors — scoped */
  .code-block .comment { color: #3f5fbf; }
  .code-block .tag { color: #7f9fbf; }
  .code-block .keyword { color: #7f0055; font-weight: bold; }
  .code-block .string { color: #2a00ff; }
  .code-block .number { color: #990000; }
  .code-block .line-comment { color: #3f7f5f; }

  /* Defensive reset (optional but recommended) */
  .code-block * {
    background: transparent;
    box-shadow: none;
  }
</style>

<pre class="code-block"><code>
<span class="comment">/**</span>
<span class="comment"> * </span><span class="tag">@author</span><span class="comment"> Premkumar Masilamani</span>
<span class="comment"> * </span><span class="tag">@company</span><span class="comment"> Tata Consultancy Services</span>
<span class="comment"> * </span><span class="tag">@about</span><span class="comment"> My Life in TCS</span>
<span class="comment"> * </span><span class="tag">@startDate</span><span class="comment"> 03-Nov-2004</span>
<span class="comment"> * </span><span class="tag">@endDate</span><span class="comment"> 21-Nov-2013</span>
<span class="comment"> */</span>

<span class="keyword">import</span> com.hindustancollege.ComputerScienceDegree;
<span class="keyword">import</span> com.love.programming.SoftwareEngineerDream;

<span class="keyword">public class</span> PremsLifeInTCS <span class="keyword">extends</span> SoftwareEngineerDream
<span class="keyword">implements</span> ComputerScienceDegree {

    <span class="keyword">public static void</span> main(String[] args) {

        <span class="line-comment">// Phase 1 - Jobless Wanderer</span>
        <span class="keyword">do</span> {
            attendInterview();
            <span class="keyword">if</span> (gotJobInTCS) {
                passedInterview = <span class="keyword">true</span>;
            }
        } <span class="keyword">while</span> (!passedInterview);

        <span class="line-comment">// Phase 2 - Learning the Trade</span>
        <span class="keyword">while</span> (working12PlusHoursADay()) {
            learnTechnology();
        }

        <span class="line-comment">// Phase 3 - Dollar Dreams</span>
        <span class="keyword">for</span> (<span class="keyword">int</span> i = <span class="number">0</span>; i &lt; <span class="number">10000</span>; i++) {
            askForOnsite();
            <span class="keyword">if</span> (yes) {
                gotoUnitedStates();
                <span class="keyword">break</span>;
            }
        }

        <span class="line-comment">// Phase 4 - Corporate Reality</span>
        <span class="keyword">if</span> (foughtWithManager() || foughtWithClient() || workedFor2Years()) {
            <span class="keyword">switch</span> (project) {
                <span class="keyword">case</span> AMEX:
                <span class="keyword">case</span> TEG:
                <span class="keyword">case</span> TFS:
                <span class="keyword">case</span> LandG:
                    <span class="keyword">break</span>;
                <span class="keyword">default</span>:
                    dontGotoOffice();
            }
        }

        <span class="line-comment">// Phase 5 - Personal Life</span>
        <span class="keyword">while</span> (notGoingToOffice()) {
            dateGirls();
            <span class="keyword">if</span> (foundTheRightOne()) {
                marryHer(<span class="string">"Love of my life"</span>);
            }
        }

        <span class="line-comment">// Phase 6 - Onsite Again</span>
        goToOnsite(
            chooseOnsite(
                maxCurrencyRate(<span class="string">"US"</span>, <span class="string">"GB"</span>, <span class="string">"SG"</span>, <span class="string">"AU"</span>)
            )
        );

        <span class="keyword">while</span> (inUnitedKingdom) {
            makeFriends();
            hostParties();
            workHard();
            <span class="keyword">if</span> (visaExpired) {
                comeBackToIndia();
                <span class="keyword">break</span>;
            }
        }

        <span class="line-comment">// Phase 7 - The Exit</span>
        <span class="keyword">if</span> (!challengingWork() && gotGoodOffer()) {
            sayGoodByeToTCS(<span class="string">"Thanks to everyone in TCS"</span>);
            pleaseKeepInTouch();
        }
    }

    <span class="keyword">public static void</span> pleaseKeepInTouch() {
        viaWebsite(<span class="string">"{{site.home}}"</span>);
        viaLinkedIn(<span class="string">"{{site.linkedin}}"</span>);
        viaGitHub(<span class="string">"{{site.github}}"</span>);

        <span class="keyword">if</span> (emergency) {
            viaPhone(<span class="string">"you-would-know-the-number"</span>);
        }
    }
}
</code></pre>
