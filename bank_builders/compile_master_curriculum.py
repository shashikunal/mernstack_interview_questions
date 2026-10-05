# compile_master_curriculum.py
import os
import sys
import json

sys.path.append(os.path.dirname(__file__))

import curriculum_data
import questions_part1
import genai_20_questions
import questions_part2
import questions_part3

def main():
    print("--- Assembling Master AI + GenAI + Vibe Coding Curriculum ---")
    
    # 1. Gather all questions
    part1_qs = questions_part1.get_part1_questions() # 30 Fund + 25 LLM = 55
    genai_qs = genai_20_questions.GENAI_20_QUESTIONS # 20 GenAI
    part2_qs = questions_part2.get_part2_questions() # 40 PE + 15 JS + 15 React + 20 API = 90
    part3_qs = questions_part3.get_part3_questions() # 20 Token + 15 RAG + 10 Sec + 10 Agents + 19 Vibe + 10 Defense = 84
    
    # Group in structured category order
    all_questions = []
    
    # Category 1: AI Fundamentals (30)
    c1 = [q for q in part1_qs if q.get("topic", "").startswith("1. AI Fundamentals")]
    # Category 2: Generative AI (20)
    c2 = genai_qs
    # Category 3: LLM Fundamentals (25)
    c3 = [q for q in part1_qs if q.get("topic", "").startswith("3. LLM Fundamentals")]
    # Category 4: Prompt Engineering (40)
    c4 = [q for q in part2_qs if q.get("topic", "").startswith("4. Prompt Engineering")]
    # Category 5: AI + JavaScript (15)
    c5 = [q for q in part2_qs if q.get("topic", "").startswith("5. AI + JavaScript")]
    # Category 6: AI + React (15)
    c6 = [q for q in part2_qs if q.get("topic", "").startswith("6. AI + React")]
    # Category 7: AI APIs (20)
    c7 = [q for q in part2_qs if q.get("topic", "").startswith("7. AI APIs")]
    # Category 8: Token Optimization (20)
    c8 = [q for q in part3_qs if q.get("topic", "").startswith("8. Token Optimization")]
    # Category 9: RAG (15)
    c9 = [q for q in part3_qs if q.get("topic", "").startswith("9. RAG")]
    # Category 10: AI Security (10)
    c10 = [q for q in part3_qs if q.get("topic", "").startswith("10. AI Security")]
    # Category 11: AI Agents (10)
    c11 = [q for q in part3_qs if q.get("topic", "").startswith("11. AI Agents")]
    # Category 12: Vibe Coding (19)
    c12 = [q for q in part3_qs if q.get("topic", "").startswith("12. Vibe Coding")]
    # Category 13: Project Architecture Defense (10)
    c13 = [q for q in part3_qs if q.get("topic", "").startswith("13. Project Architecture")]
    
    all_ordered_categories = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13]
    
    global_idx = 1
    for cat in all_ordered_categories:
        for q in cat:
            item = dict(q)
            # Ensure proper subject and schema consistency
            item["subject"] = "AI & Generative AI"
            item["id"] = f"ai_q_{global_idx:03d}"
            # Ensure options exist
            if "options" not in item or len(item["options"]) < 4:
                item["options"] = [
                    item.get("answer", "")[:120] + "...",
                    "Alternative theoretical approach without practical production implementation",
                    "Deprecated legacy method not recommended for modern enterprise codebases",
                    "Client-side fallback only applicable in development sandbox environments"
                ]
                item["correctIndex"] = 0
            all_questions.append(item)
            global_idx += 1
            
    print(f"Total Questions compiled: {len(all_questions)}")
    for i, cat in enumerate(all_ordered_categories, 1):
        if cat:
            print(f"  Cat {i} ({cat[0].get('topic')}): {len(cat)} questions")
            
    # Course Steps & Videos & Prompt Exercises
    steps = curriculum_data.COURSE_STEPS
    videos = curriculum_data.VIDEO_LESSONS
    prompts = curriculum_data.PROMPT_EXERCISES
    
    print(f"Steps: {len(steps)}, Videos: {len(videos)}, Prompt Exercises: {len(prompts)}")
    
    # Generate JavaScript file
    js_content = f"""/**
 * Complete AI + Generative AI + Prompt Engineering + Vibe Coding Module
 * Comprehensive practical curriculum, video demonstrations, prompt analyzer, and 249 genuine interview questions.
 * Generated automatically by compile_master_curriculum.py
 */

(function() {{
  const AI_QUESTIONS = {json.dumps(all_questions, indent=2, ensure_ascii=False)};

  const AI_VIBE_COURSE_DATA = {{
    metadata: {{
      title: "AI + Generative AI + Prompt Engineering + Vibe Coding Master Course",
      tagline: "Understand → Practice → Use AI Tools → Vibe Code → Build → Test → Optimize → Explain → Interview",
      totalSteps: {len(steps)},
      totalVideos: {len(videos)},
      totalPromptExercises: {len(prompts)},
      totalInterviewQuestions: {len(all_questions)},
      version: "2.0.0"
    }},
    steps: {json.dumps(steps, indent=2, ensure_ascii=False)},
    videos: {json.dumps(videos, indent=2, ensure_ascii=False)},
    promptExercises: {json.dumps(prompts, indent=2, ensure_ascii=False)}
  }};

  // Expose to window for clean-reader and direct consumption
  window.AI_GENAI_QUESTIONS_DATA = AI_QUESTIONS;
  window.AI_VIBE_COURSE_DATA = AI_VIBE_COURSE_DATA;

  console.log(`[AI Curriculum] Loaded ${{AI_QUESTIONS.length}} interview questions, ${{AI_VIBE_COURSE_DATA.steps.length}} steps, ${{AI_VIBE_COURSE_DATA.videos.length}} videos, ${{AI_VIBE_COURSE_DATA.promptExercises.length}} prompt exercises.`);
}})();
"""

    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    out_curriculum = os.path.join(workspace_root, "ai-vibe-curriculum.js")
    with open(out_curriculum, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Wrote {out_curriculum} ({len(js_content)} bytes)")
    
    # Also overwrite ai-genai-data.js so existing script tag loads it directly
    out_ai_data = os.path.join(workspace_root, "ai-genai-data.js")
    with open(out_ai_data, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Wrote {out_ai_data} ({len(js_content)} bytes)")

if __name__ == "__main__":
    main()
